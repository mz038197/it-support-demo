import pytest

from it_tools.disk import needs_alert, usage_percent


def test_usage_percent():
    assert usage_percent(45, 100) == 45.0


def test_zero_total():
    with pytest.raises(ValueError):
        usage_percent(1, 0)


def test_needs_alert():
    assert needs_alert(95, 100)
    assert not needs_alert(50, 100)
