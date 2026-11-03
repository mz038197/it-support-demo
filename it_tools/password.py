"""密碼規則檢查。"""

MIN_LENGTH = 8


def is_strong_password(password: str) -> bool:
    """密碼至少 MIN_LENGTH 個字元，而且同時有大寫、小寫和數字。"""
    return (
        len(password) >= MIN_LENGTH
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
    )
