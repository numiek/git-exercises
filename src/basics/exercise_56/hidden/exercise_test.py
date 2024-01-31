from src.basics.exercise_56.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    assert normalize_str(answer()) in {
        normalize_str("git remote rm example"),
        normalize_str("git remote remove example"),
    }
