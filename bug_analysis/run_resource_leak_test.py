#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

"""
This script runs the test for the resource leak fix in GeometrySimplificationBenchmark.java
"""

def run_test():
    print("Attempting to run the resource leak test...")
    
    # First, let's examine the original file to confirm the issue
    benchmark_file = Path("/home/ubuntu/cursor_conversion/benchmarks/src/main/java/org/elasticsearch/benchmark/spatial/GeometrySimplificationBenchmark.java")
    
    if not benchmark_file.exists():
        print(f"Error: Could not find the benchmark file at {benchmark_file}")
        return False
    
    print(f"Found benchmark file: {benchmark_file}")
    
    # We can't actually run the test directly since it would require the full Elasticsearch build system
    # Instead, we'll verify the issue exists and prepare a fix
    
    with open(benchmark_file, 'r') as f:
        content = f.read()
    
    # Check if the issue exists
    if "BufferedReader reader = new BufferedReader" in content and "reader.close()" not in content:
        print("Confirmed issue: BufferedReader is created but not closed properly")
        return True
    else:
        print("Could not confirm the resource leak issue in the file")
        return False

def main():
    if run_test():
        print("Test verification successful. Ready to implement the fix.")
    else:
        print("Test verification failed. Please check the file manually.")

if __name__ == "__main__":
    main()
