from it_tools.password import is_strong_password


def test_strong_password():
    assert is_strong_password("Abcdefg1")


def test_missing_digit():
    assert not is_strong_password("Abcdefgh")


def test_too_short():
    assert not is_strong_password("Ab1")
