#!/usr/bin/env python3

"""
Node Modules Finder

This script recursively searches for node_modules directories and calculates their sizes.
It can be used standalone or in conjunction with node_cleaner.sh for directory removal.

Features:
- Recursive directory traversal
- Size calculation in MB
- Human-readable or JSON output
- Click-based CLI interface
- Colorized output

Usage:
    ./main.py [OPTIONS] [SEARCH_PATH]

Options:
    --json-output  Output in machine-readable format for shell script integration
    --help        Show this message and exit.
"""

import os
import sys
import click
from colorama import Fore, Style, init

# Initialize colorama for cross-platform colored output
init()

def get_size(path):
    """
    Calculate the total size of a directory in megabytes.
    
    Args:
        path (str): Path to the directory
        
    Returns:
        float: Size in megabytes
        
    Note:
        Handles permission errors silently to avoid script interruption
    """
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
    except Exception:
        pass
    return total / (1024 * 1024)  # Convert to MB

@click.command()
@click.argument('search_path', type=click.Path(exists=True), default='/Users/ahmad/dev/wb_projects')
@click.option('--json-output', is_flag=True, help='Output in machine-readable format')
def main(search_path, json_output):
    """
    Find all node_modules directories and their sizes.
    
    Args:
        search_path (str): Directory to search in (default: /Users/ahmad/dev/wb_projects)
        json_output (bool): If True, output in format suitable for shell script parsing
    
    The script will recursively search for node_modules directories starting from
    the specified path. For each directory found, it calculates and displays its size.
    
    Output formats:
    - Normal: Colored, human-readable output
    - JSON: pipe-separated values (path|size) for shell script parsing
    """
    for root, dirs, _ in os.walk(search_path):
        if 'node_modules' in dirs:
            path = os.path.join(root, 'node_modules')
            size = get_size(path)
            if json_output:
                # Output in format that shell script can easily parse
                print(f"{path}|{size:.2f}")
            else:
                # Human readable output
                print(f"{Fore.YELLOW}Found: {path} ({size:.2f} MB){Style.RESET_ALL}")

if __name__ == "__main__":
    main()
