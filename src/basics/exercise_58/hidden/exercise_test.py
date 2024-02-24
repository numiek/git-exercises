import functools
from src.basics.exercise_58.exercise import answer
from src.hidden.normalize_str import normalize_str


def test_answer():
    str_normalizer = functools.partial(normalize_str, is_case_sensitive=True)
    assert str_normalizer(answer()) == str_normalizer('git tag -l "v.1.???.5*"')
