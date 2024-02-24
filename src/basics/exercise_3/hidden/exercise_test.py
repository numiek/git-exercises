from src.basics.exercise_3.exercise import get_stage_command
import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = ("./dir/file.txt",)
    command_template = "git add {}"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)

    assert str_normalizer(get_stage_command()) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
