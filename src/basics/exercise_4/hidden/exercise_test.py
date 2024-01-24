from src.basics.exercise_4.exercise import get_state_command


def test_get_state_command():
    assert get_state_command() == "git status"
