import re


def reverse_string(text: str) -> str:
    return text[::-1]


def is_palindrome(text: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned == cleaned[::-1]


def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


def to_title_case(text: str) -> str:
    return " ".join(word.capitalize() for word in text.strip().split())


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"[\s_-]+", "-", cleaned)


def truncate_string(text: str, max_length: int) -> str:
    if max_length < 0:
        raise ValueError("max_length cannot be negative.")
    if len(text) <= max_length:
        return text
    if max_length <= 3:
        return text[:max_length]
    return text[: max_length - 3] + "..."
