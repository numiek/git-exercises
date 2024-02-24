import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.basics.exercise_62.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = (
        "repo",
        "v1.0.0",
    )
    command_template = "git push {} {}"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)

    assert str_normalizer(answer()) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
