"""
Problem Description:
    Implement a function 'create_glob_patterns' that returns a list of glob patterns, 
    each designed to solve specific predefined file matching tasks.

    Tasks for the glob patterns:
    1. Match all .txt files in the current directory.
    2. Match all .jpg files in any subdirectory.
    3. Match any files with a single character name (any extension) in the current directory.
    4. Match all files and directories in any level of subdirectories under 'docs'.
    5. Match all files that start with 'data_' and end with '.csv' in the current directory.
    6. Match all Python files (.py) in the immediate subdirectories.
    7. Match all files in directories that start with '2023_' at any directory level.
    8. Match all files with extensions that have exactly four characters in all subdirectories.
    9. Match all files and directories in directories that start with '2023_' at any directory level.
"""


def create_glob_patterns():
    return [
        "",  # 1. Match all .txt files in the current directory.
        "",  # 2. Match all .jpg files in any subdirectory.
        "",  # 3. Match any files with a single character name (any extension) in the current directory.
        "",  # 4. Match all files and directories in any level of subdirectories under 'docs'.
        "",  # 5. Match all files that start with 'data_' and end with '.csv' in the current directory.
        "",  # 6. Match all Python files (.py) in the immediate subdirectories.
        "",  # 7. Match all files in directories that start with '2023_' at any directory level.
        "",  # 8. Match all files with extensions that have exactly four characters in all subdirectories.
        "",  # 9. Match all files and directories in directories that start with '2023_' at any directory level.
    ]
