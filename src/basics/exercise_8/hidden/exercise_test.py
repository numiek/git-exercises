import pathlib


DIR_PATH = pathlib.Path(__file__).parent.parent


def test_gitignore_specific_files():
    with open(DIR_PATH / ".gitignore", "r") as f:
        lines = f.read().strip()

    assert "/secrets_*" in lines
    assert "!/secrets_test.txt" in lines
