import functools
from src.basics.exercise_6.exercise import create_glob_patterns
from src.hidden.normalize_iterable import normalize_iterable


def test():
    iterable_normalizer = functools.partial(normalize_iterable, is_case_sensitive=True)

    assert iterable_normalizer(create_glob_patterns()) == iterable_normalizer(
        [
            "./*.txt",  # 1. Match all .txt files in the current directory.
            "./**/*.jpg",  # 2. Match all .jpg files in any subdirectory.
            "./?.*",  # 3. Match any files with a single character name (any extension) in the current directory.
            "./docs/**/*.*",  # 4. Match all files in any level of subdirectories under 'docs'.
            "./data_*.csv",  # 5. Match all files that start with 'data_' and end with '.csv' in the current directory.
            "./*/*.py",  # 6. Match all Python files (.py) in the immediate subdirectories.
            "./**/2023_*/*.*",  # 7. Match all files in directories that start with '2023_' at any directory level.
            "./**/*.????",  # 8. Match all files with extensions that have exactly four characters.
        ]
    )
