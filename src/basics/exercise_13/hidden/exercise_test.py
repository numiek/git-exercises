from src.basics.exercise_13.exercise import answer


def test_answer():
    assert answer() == "git diff --staged"
