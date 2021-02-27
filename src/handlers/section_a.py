from models.response import VowelSummary


def get_vowels_summary(line: str) -> VowelSummary:
    """
    Return the amount of vowels and a new line with vowels changed
    """
    if not isinstance(line, str):
        raise ValueError("line must be str")

    vowels_eq = {
        "a": "e", "A": "E",
        "e": "i", "E": "I",
        "i": "o", "I": "O",
        "o": "u", "O": "U",
        "u": "a", "U": "A",
    }

    result = {"vowels_count": 0, "new_line": ""}

    for l in line:
        result.update({
            "vowels_count": result.get("vowels_count") + int(l in vowels_eq.keys()),
            "new_line": result.get("new_line") + vowels_eq.get(l, l),
        })

    return VowelSummary(**result)
