from src.basics.exercise_64.exercise import answer
import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = ("file1.txt",)
    command_template = "git rm {}"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)
    a, b = answer()

    assert str_normalizer(a) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
    assert b is True
