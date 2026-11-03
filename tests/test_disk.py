import pytest

from it_tools.disk import usage_percent


def test_usage_percent():
    assert usage_percent(45, 100) == 45.0


def test_zero_total():
    with pytest.raises(ValueError):
        usage_percent(1, 0)
