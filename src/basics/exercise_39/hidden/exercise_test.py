from src.hidden.normalize_str import normalize_str
from src.basics.exercise_39.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        r'git log --before="2 weeks ago" -P --author="^N[^\W_\d]*\s+K[^\W_\d]*$" --author="^Max Huf[^\W_\d]*$"'
    )
