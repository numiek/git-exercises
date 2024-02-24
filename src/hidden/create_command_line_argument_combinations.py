from collections.abc import Iterable, Generator
import itertools


def create_command_line_argument_combinations(
    arguments: Iterable[str],
) -> Generator[tuple[str, ...], None, None]:
    argument_variations = tuple([argument.replace('"', ""), f'"{argument.replace('"', "")}"'] for argument in arguments)

    for combination in itertools.product(*argument_variations):
        yield tuple(combination)
