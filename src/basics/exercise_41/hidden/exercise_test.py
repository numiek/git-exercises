from src.hidden.normalize_str import normalize_str
from src.basics.exercise_41.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        r'git log -P --committer="^Max Lean$" -S "my_function("'
    )
