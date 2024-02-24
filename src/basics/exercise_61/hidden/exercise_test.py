import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.basics.exercise_61.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = (
        "v1.0.0",
        "166ae0c4d3f420721acbb115cc33848dfcc2121a",
    )
    command_template = "git tag -a {} {}"
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)

    assert str_normalizer(answer()) in {
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
    }
