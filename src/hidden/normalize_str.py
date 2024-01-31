def normalize_str(string: str, is_case_sensitive: bool = False) -> str:
    string = " ".join(string.strip().split())

    if not is_case_sensitive:
        string = string.casefold()

    return string
