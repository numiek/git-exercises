from src.hidden.normalize_str import normalize_str
from src.basics.exercise_42.exercise import answer


def test_answer():
    assert normalize_str(answer()) in {
        normalize_str(
            r'git log --no-merges --before="2000-01-01 15:00:00" --name-only -- ./files/'
        ),
        normalize_str(
            r'git log --no-merges --before="2000-01-01 15:00:00" --name-status -- ./files/'
        ),
        normalize_str(
            r'git log --no-merges --before="2000-01-01 15:00:00" --stat -- ./files/'
        ),
    }
