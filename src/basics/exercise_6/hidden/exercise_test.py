import pathlib
import pytest
import glob
from exercise import create_glob_patterns
from src.basics.exercise_6.exercise import create_glob_patterns


# Function to setup test environment in a temporary directory
def setup_test_environment(tmp_path, paths):
    for path in paths:
        file_path = tmp_path / path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.touch()
        with open(file_path, "w") as f:
            f.write("test content")
    return tmp_path


# Utility function to verify glob patterns
def verify(tmp_path, expected, glob_pattern):
    assert sorted(
        pathlib.Path(path).resolve()
        for path in glob.glob(str(tmp_path / glob_pattern), recursive=True)
    ) == sorted(tmp_path / pathlib.Path(path) for path in expected)


@pytest.fixture
def glob_patterns(tmp_path):
    # Common paths used in the tests
    paths = [
        "file.txt",
        "a.txt",
        "data_001.csv",
        "test.py",
        "subdir/image.jpg",
        "subdir/script.py",
        "docs/doc.txt",
        "docs/deep/subdoc.txt",
        "2023_data/log.txt",
        "file.ext",
        "single/a.ext",
        "single/b.txt",
        "2023_reports/report.pdf",
        "data_002.csv",
        "randomfile.ext",
        "anyfolder1/anyfolder2/file.abcd",
        "anyfolder2/file.abcd",
        "file.abcd",
    ]
    setup_test_environment(tmp_path, paths)
    return create_glob_patterns()


# Test for each specific glob pattern task
def test_txt_files_current_directory(glob_patterns, tmp_path):
    expected = ["file.txt", "a.txt"]
    verify(tmp_path, expected, glob_patterns[0])


def test_jpg_files_subdirectories(glob_patterns, tmp_path):
    expected = ["subdir/image.jpg"]
    verify(tmp_path, expected, glob_patterns[1])


# Additional tests for each task
def test_single_character_filenames(glob_patterns, tmp_path):
    expected = ["a.txt"]
    verify(tmp_path, expected, glob_patterns[2])


def test_files_in_docs_subdirectories(glob_patterns, tmp_path):
    expected = ["docs/doc.txt", "docs/deep/subdoc.txt"]
    verify(tmp_path, expected, glob_patterns[3])


def test_data_csv_files_current_directory(glob_patterns, tmp_path):
    expected = ["data_001.csv", "data_002.csv"]
    verify(tmp_path, expected, glob_patterns[4])


def test_python_files_in_immediate_subdirectories(glob_patterns, tmp_path):
    expected = ["subdir/script.py"]
    verify(tmp_path, expected, glob_patterns[5])


def test_files_in_directories_starting_with_2023(glob_patterns, tmp_path):
    expected = ["2023_data/log.txt", "2023_reports/report.pdf"]
    verify(tmp_path, expected, glob_patterns[6])


def test_files_with_four_character_extensions(glob_patterns, tmp_path):
    expected = ["anyfolder1/anyfolder2/file.abcd", "anyfolder2/file.abcd", "file.abcd"]
    verify(tmp_path, expected, glob_patterns[7])


# Ensure tests cover all the tasks defined in the exercise
