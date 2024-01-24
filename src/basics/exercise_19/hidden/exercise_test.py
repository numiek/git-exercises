import subprocess
from src.basics.exercise_19.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    command, flag = answer()

    assert (
        normalize_str(command),
        flag,
    ) == (
        normalize_str("git rm file1.txt"),
        True,
    )
