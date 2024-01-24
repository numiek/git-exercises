from src.hidden.normalize_str import normalize_str
from src.basics.exercise_27.exercise import answer


def test_answer():
    options = {
        normalize_str(option)
        for option in ["git log --pretty=oneline", 'git log --pretty="oneline"']
    }
    assert normalize_str(answer()) in options
