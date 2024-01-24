import pathlib


def test_basic_gitignore():
    with open(pathlib.Path(__file__).parent.parent / ".gitignore", "r") as f:
        lines = f.readlines()

    assert "*.log\n" in lines, "Failed to ignore .log files"
    assert "temp\n" in lines, "Failed to ignore temp/ directory"
