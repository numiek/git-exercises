from src.basics.exercise_20.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    command, flag = answer()

    assert (
        normalize_str(command),
        flag,
    ) == (
        normalize_str("git rm -f file1.txt"),
        True,
    )
