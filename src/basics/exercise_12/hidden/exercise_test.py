import subprocess
from src.basics.exercise_12.exercise import answer


def setup_repo_with_files(tmp_path):
    files_path = tmp_path / "files"
    fake_path = tmp_path / "fake"
    files_path.mkdir()
    fake_path.mkdir()

    # Create sample .txt files
    for i in range(3):
        with open(files_path / f"file{i}.txt", "w") as f:
            f.write(f"Sample content {i}")

        with open(fake_path / f"fake{i}.txt", "w") as f:
            f.write(f"Sample content {i}")

    # Initialize git repository
    subprocess.run(["git", "init"], cwd=tmp_path)
    return tmp_path


def test_stage_txt_files(tmp_path):
    repo_path = setup_repo_with_files(tmp_path)

    command = answer()
    subprocess.run(command.split(), cwd=repo_path)  # Execute the returned Git command

    # Check if the correct files are staged
    staged_files = (
        subprocess.run(
            ["git", "diff", "--name-only", "--cached"],
            capture_output=True,
            text=True,
            cwd=repo_path,
        )
        .stdout.strip()
        .split("\n")
    )

    assert all(
        file.startswith("files/") and file.endswith(".txt") for file in staged_files
    ), "Not all .txt files in 'files/' were correctly staged"
