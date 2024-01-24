from src.basics.exercise_1.exercise import initialize_git


def test_git_initialization():
    assert initialize_git() == "git init ./subdir"
