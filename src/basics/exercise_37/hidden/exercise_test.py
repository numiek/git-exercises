from src.hidden.normalize_str import normalize_str
from src.basics.exercise_37.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        'git log --after="1 day 2 weeks 2 hours 3 minutes ago"'
    )
