from src.hidden.normalize_str import normalize_str
from src.basics.exercise_38.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        'git log --before="2000-01-01 13:55:00"'
    )
