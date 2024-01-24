import subprocess
from src.basics.exercise_18.exercise import answer


def setup_git_repo(tmp_path):
    repo_path = tmp_path
    file_path = repo_path / "sample.txt"
    file_path.write_text("Initial content\n")

    # Initialize git repository and make an initial commit
    subprocess.run(["git", "init"], cwd=repo_path)
    subprocess.run(["git", "add", "sample.txt"], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo_path)

    return repo_path, file_path


def test_amend_last_commit(tmp_path):
    repo_path, file_path = setup_git_repo(tmp_path)

    # Make some changes to the file
    file_path.write_text("Modified content\n")

    # Execute the commands returned by answer function sequentially
    commands = answer()
    for command in commands:
        subprocess.run(command, shell=True, cwd=repo_path)

    # Check the content and message of the last commit
    last_commit_msg = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"],
        capture_output=True,
        text=True,
        cwd=repo_path,
    ).stdout.strip()
    last_commit_content = file_path.read_text()

    assert (
        last_commit_msg == "small adjustment"
    ), "The commit message was not correctly amended"
    assert (
        last_commit_content == "Modified content\n"
    ), "The file content was not correctly amended in the last commit"


def test_amend_without_changes(tmp_path):
    repo_path, _ = setup_git_repo(tmp_path)

    # Execute the commands returned by answer function sequentially without making changes
    commands = answer()
    for command in commands:
        subprocess.run(command, shell=True, cwd=repo_path)

    # Check if 'git commit -a --amend -m "small adjustment"' creates a new commit when there are no changes
    result = subprocess.run(
        ["git", "log", "-2", "--pretty=%B"],
        capture_output=True,
        text=True,
        cwd=repo_path,
    ).stdout.strip()
    commit_messages = result.split("\n")

    assert (
        len(commit_messages) == 1 and commit_messages[0] == "small adjustment"
    ), "A new commit was created or the commit message was not amended correctly"
