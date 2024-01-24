import pathlib

GITIGNORE_PATH = pathlib.Path(__file__).parent.parent / ".gitignore"


def test_advanced_gitignore_patterns():
    assert GITIGNORE_PATH.exists(), ".gitignore file does not exist"

    with open(GITIGNORE_PATH, "r") as gitignore_file:
        gitignore_content = gitignore_file.read()

    print(gitignore_content)

    # Check for pattern to ignore all '.tmp' files in any subdirectory
    assert (
        "**/*.tmp" in gitignore_content
    ), "Missing pattern to ignore '.tmp' files in subdirectories"

    # Check for pattern to ignore 'logs/' directory only at the root level
    assert (
        "logs/" in gitignore_content
    ), "Missing pattern to ignore 'logs/' directory at the root level"
