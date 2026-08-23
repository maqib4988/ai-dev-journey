def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]