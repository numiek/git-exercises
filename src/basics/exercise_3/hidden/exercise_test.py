from src.basics.exercise_3.exercise import get_stage_command


def test_get_stage_command():
    assert get_stage_command() == "git add ./dir/file.txt"
