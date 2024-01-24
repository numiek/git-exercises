from src.hidden.normalize_str import normalize_str
from src.basics.exercise_29.exercise import answer


def test_answer():
    options = {
        normalize_str(option)
        for option in ["git log --pretty=full", 'git log --pretty="full"']
    }
    assert normalize_str(answer()) in options
