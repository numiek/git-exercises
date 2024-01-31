from src.hidden.normalize_str import normalize_str
from src.basics.exercise_48.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str("git remote -v")
