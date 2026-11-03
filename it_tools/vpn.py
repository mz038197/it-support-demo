"""VPN 設定檔檢查。"""

DEFAULT_TIMEOUT_SECONDS = 30


def validate_vpn_config(config: dict) -> list[str]:
    """回傳設定檔的錯誤清單。清單是空的，代表設定正確。"""
    errors = []
    if not config.get("server"):
        errors.append("缺少 server")
    port = config.get("port", 1194)
    if not 1 <= port <= 65535:
        errors.append(f"port 超出範圍：{port}")
    timeout = config.get("timeout", DEFAULT_TIMEOUT_SECONDS)
    if timeout <= 0:
        errors.append(f"timeout 必須大於 0：{timeout}")
    return errors
