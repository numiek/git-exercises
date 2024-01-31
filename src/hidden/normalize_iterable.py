from collections.abc import Iterable
from src.hidden.normalize_str import normalize_str


def normalize_iterable(
    iterable: Iterable[str], is_case_sensitive: bool = False
) -> tuple[str, ...]:
    return tuple(
        normalize_str(element, is_case_sensitive=is_case_sensitive)
        if isinstance(element, str)
        else element
        for element in iterable
    )
