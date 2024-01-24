import pathlib


DIR_PATH = pathlib.Path(__file__).parent.parent


def test_gitignore_specific_files():
    with open(DIR_PATH / ".gitignore", "r") as f:
        lines = f.read().splitlines()

    assert "secrets.txt" in lines, "Failed to ignore 'secrets.txt'"
    assert "config.txt" not in lines, "'config.txt' should not be ignored"
