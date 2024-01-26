from src.hidden.normalize_str import normalize_str
from src.basics.exercise_40.exercise import answer


def test_answer():
    assert normalize_str(answer()) == normalize_str(
        r'git log -P --committer="^Max F[^\W_\d]*$" --grep="\[IMPORTANT-\d\]"'
    )
