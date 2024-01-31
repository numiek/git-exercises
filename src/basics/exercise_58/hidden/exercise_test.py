from src.basics.exercise_58.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        r'git tag -l "^[[:digit:]]{1,}\.[[:digit:]]\.[[:digit:]]{3}$"'
    )
