from src.hidden.normalize_str import normalize_str
from src.basics.exercise_31.exercise import answer


def test_answer():
    assert normalize_str(answer()) in normalize_str('git log --pretty="format:<value>"')
