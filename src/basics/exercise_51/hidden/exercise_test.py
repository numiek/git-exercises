from src.hidden.normalize_iterable import normalize_iterable
from src.basics.exercise_51.exercise import answer



def test_answer():
    is_case_sensitive = True
    assert normalize_iterable(
        answer(), is_case_sensitive=is_case_sensitive
    ) == normalize_iterable(
        (
            "git fetch example",
            "example/br",
        ),
        is_case_sensitive=is_case_sensitive,
    )
    
