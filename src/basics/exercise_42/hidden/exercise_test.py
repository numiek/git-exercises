from src.basics.exercise_42.exercise import answer
from src.hidden.normalize_str import normalize_str
import functools
from src.hidden.create_command_line_argument_combinations import (
    create_command_line_argument_combinations,
)
from src.hidden.normalize_str import normalize_str


def test_answer():
    arguments = ("./files/",)
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)
    command_templates = [
        'git log --no-merges --before="2000-01-01 15:00:00" --name-only -- {}',
        'git log --no-merges --before="2000-01-01 15:00:00" --name-status -- {}',
        'git log --no-merges --before="2000-01-01 15:00:00" --stat -- {}',
    ]

    assert str_normalizer(answer()) in (
        str_normalizer(command_template.format(*combination))
        for combination in create_command_line_argument_combinations(arguments)
        for command_template in command_templates
    )
