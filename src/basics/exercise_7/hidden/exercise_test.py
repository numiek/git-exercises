import pathlib


def test_basic_gitignore():
    content = None

    with open(pathlib.Path(__file__).parent.parent / ".gitignore", "r") as f:
        content = f.read()

    assert "/*.log" in content
    assert (
        "/temp/" in content
        or "/temp/**/" in content
        or "/temp/**/*" in content
        or "/temp/**/" in content
    )
    assert (
        "/**/invalid/" in content
        or "invalid/" in content
        or "invalid/**/*" in content
        or "/**/invalid/**/*" in content
        or "/**/invalid/**/" in content
    )
