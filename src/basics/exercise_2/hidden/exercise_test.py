from src.basics.exercise_2.exercise import copy_git


def test_copy_git():
    assert copy_git() == "git clone https://example.com ./subdir"
