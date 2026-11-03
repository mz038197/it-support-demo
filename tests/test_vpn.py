from it_tools.vpn import DEFAULT_TIMEOUT_SECONDS, validate_vpn_config


def test_valid_config():
    assert validate_vpn_config({"server": "vpn.example.com"}) == []


def test_missing_server():
    assert "缺少 server" in validate_vpn_config({})


def test_default_timeout():
    assert DEFAULT_TIMEOUT_SECONDS == 5
