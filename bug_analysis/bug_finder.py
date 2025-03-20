#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from concurrent.futures import ProcessPoolExecutor
from collections import defaultdict

"""
Bug Finder for Elasticsearch Codebase

This script analyzes Java files in the Elasticsearch codebase to identify potential bugs
in the following categories:
1. Resource leaks (unclosed streams, readers, etc.)
2. Null pointer dereferences
3. Concurrency issues (improper synchronization)
4. Exception handling issues
5. Potential infinite loops
6. Unused variables and imports

Usage: python bug_finder.py [path_to_codebase]
"""

# Common patterns for potential bugs
PATTERNS = {
    "resource_leak": [
        r"new FileInputStream\([^)]+\)(?!.*\.close\(\))",
        r"new FileOutputStream\([^)]+\)(?!.*\.close\(\))",
        r"new BufferedReader\([^)]+\)(?!.*\.close\(\))",
        r"new BufferedWriter\([^)]+\)(?!.*\.close\(\))",
    ],
    "null_pointer": [
        r"(\w+)\s*=\s*null[^;]*;\s*(?:[^;]*;)*\s*\1\.([\w\(\)]+)",
        r"return\s+\w+\.\w+\(\)\s*(?://.*)?$",
        r"if\s*\(\s*\w+\s*!=\s*null\s*\)\s*\{\s*\}(?!\s*else)",
    ],
    "concurrency_issue": [
        r"(?<!synchronized)\s+void\s+\w+\([^)]*\)\s*\{[^}]*(?:this|super)\.\w+\s*=",
        r"(?<!volatile)\s+\w+\s+\w+\s*=\s*[^;]+;\s*(?://.*)?$\s*(?:public|private|protected)",
        r"synchronized\s*\(\s*new\s+\w+",
    ],
    "exception_handling": [
        r"catch\s*\([^)]+\)\s*\{\s*\}",
        r"catch\s*\([^)]+\)\s*\{\s*e\.printStackTrace\(\);\s*\}",
        r"throw\s+new\s+\w+Exception\([^)]*\)\s*;\s*(?://.*)?$",
    ],
    "infinite_loop": [
        r"while\s*\(\s*true\s*\)\s*\{(?![^}]*break)",
        r"for\s*\([^;]*;\s*;\s*[^)]*\)\s*\{(?![^}]*break)",
    ],
    "unused_code": [
        r"private\s+\w+\s+(\w+)\s*(?:=\s*[^;]+)?;\s*(?://.*)?$(?!.*\1)",
        r"import\s+[^;]+;\s*(?://.*)?$(?!.*\b\w+\b)",
    ],
}

def find_java_files(base_path):
    """Find all Java files in the given directory."""
    java_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

def analyze_file(file_path):
    """Analyze a single Java file for potential bugs."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return file_path, {"error": str(e)}
    
    results = defaultdict(list)
    
    for bug_type, patterns in PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, content, re.MULTILINE):
                line_number = content[:match.start()].count('\n') + 1
                line_content = content.split('\n')[line_number - 1].strip()
                results[bug_type].append({
                    "line": line_number,
                    "content": line_content,
                    "match": match.group(0)
                })
    
    return file_path, dict(results)

def analyze_codebase(base_path, max_workers=8, max_files=None):
    """Analyze the entire codebase for potential bugs."""
    java_files = find_java_files(base_path)
    
    if max_files:
        java_files = java_files[:max_files]
    
    print(f"Found {len(java_files)} Java files to analyze")
    
    results = {}
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for file_path, file_results in executor.map(analyze_file, java_files):
            if file_results:  # Only store files with potential issues
                results[file_path] = file_results
    
    return results

def format_results(results):
    """Format the analysis results for output."""
    output = []
    bug_count = defaultdict(int)
    
    for file_path, file_results in results.items():
        if "error" in file_results:
            output.append(f"Error analyzing {file_path}: {file_results['error']}")
            continue
        
        has_issues = False
        file_output = [f"\n## {os.path.relpath(file_path)}"]
        
        for bug_type, issues in file_results.items():
            if issues:
                has_issues = True
                bug_count[bug_type] += len(issues)
                file_output.append(f"\n### {bug_type.replace('_', ' ').title()} ({len(issues)})")
                
                for issue in issues:
                    file_output.append(f"- Line {issue['line']}: `{issue['content']}`")
        
        if has_issues:
            output.extend(file_output)
    
    summary = ["# Bug Analysis Summary\n"]
    summary.append(f"Analyzed {len(results)} Java files with potential issues\n")
    
    if bug_count:
        summary.append("## Bug Count by Type\n")
        for bug_type, count in bug_count.items():
            summary.append(f"- {bug_type.replace('_', ' ').title()}: {count}")
        summary.append("\n")
    else:
        summary.append("No potential bugs found.\n")
    
    return "\n".join(summary + output)

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else ".."
    max_files = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    print(f"Analyzing Java files in {base_path}...")
    results = analyze_codebase(base_path, max_files=max_files)
    
    output = format_results(results)
    
    output_file = "bug_analysis_report.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Analysis complete. Results written to {output_file}")

if __name__ == "__main__":
    main()
