from src.hidden.normalize_str import normalize_str
from src.basics.exercise_44.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str("git rm file1.txt --cached")
