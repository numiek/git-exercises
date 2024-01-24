from src.basics.exercise_32.exercise import answer


def test_answer():
    assert answer() == {
        "commit hash (full)": "%H",
        "commit hash (short)": "%h",
        "author name": "%an",
        "author email": "%ae",
        "author date (absolute)": "%ad",
        "author date (relative)": "%ar",
        "committer name": "%cn",
        "committer email": "%ce",
        "committer date (absolute)": "%cd",
        "committer date (relative)": "%cr",
        "subject": "%s",
    }
