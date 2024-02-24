import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.basics.exercise_63.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = ("repo",)
    command_template = "git push {} --tags"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)

    assert str_normalizer(answer()) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
