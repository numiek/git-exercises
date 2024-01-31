from src.basics.exercise_52.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    assert normalize_str(answer()) == normalize_str("git pull")
