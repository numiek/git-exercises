from src.basics.exercise_2.exercise import copy_git
import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = (
        "https://example.com",
        "./subdir",
    )
    command_template = "git clone {} {}"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)

    assert str_normalizer(copy_git()) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
