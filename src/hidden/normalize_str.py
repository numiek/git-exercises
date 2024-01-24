def normalize_str(string: str) -> str:
    return " ".join(string.strip().split()).casefold()
