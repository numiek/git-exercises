from src.basics.exercise_5.exercise import get_short_state_command


def test_get_short_state_command():
    assert get_short_state_command() == "git status -s"
