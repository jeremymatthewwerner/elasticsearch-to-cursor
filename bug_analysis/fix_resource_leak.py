#!/usr/bin/env python3
import os
import sys
from pathlib import Path

"""
This script fixes the resource leak in GeometrySimplificationBenchmark.java
by ensuring the BufferedReader is properly closed.
"""

def fix_resource_leak():
    benchmark_file = Path("/home/ubuntu/cursor_conversion/benchmarks/src/main/java/org/elasticsearch/benchmark/spatial/GeometrySimplificationBenchmark.java")
    
    if not benchmark_file.exists():
        print(f"Error: Could not find the benchmark file at {benchmark_file}")
        return False
    
    print(f"Found benchmark file: {benchmark_file}")
    
    # Read the original file
    with open(benchmark_file, 'r') as f:
        content = f.read()
    
    # Create a backup of the original file
    backup_file = benchmark_file.with_suffix('.java.bak')
    with open(backup_file, 'w') as f:
        f.write(content)
    print(f"Created backup at: {backup_file}")
    
    # Fix the resource leak by using try-with-resources
    fixed_content = content.replace(
        "BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));",
        "try (BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8))) {"
    )
    
    # Add closing brace after the reader usage
    fixed_content = fixed_content.replace(
        "return builder.toString();",
        "    return builder.toString();\n        }"
    )
    
    # Write the fixed content back to the file
    with open(benchmark_file, 'w') as f:
        f.write(fixed_content)
    
    print(f"Fixed resource leak in: {benchmark_file}")
    return True

def main():
    if fix_resource_leak():
        print("Successfully fixed the resource leak bug.")
    else:
        print("Failed to fix the resource leak bug.")

if __name__ == "__main__":
    main()
