"""磁碟用量計算。"""


def usage_percent(used_gb: float, total_gb: float) -> float:
    """回傳用量百分比，取到小數第一位。"""
    if total_gb <= 0:
        raise ValueError("total_gb 必須大於 0")
    return round(used_gb / total_gb * 100, 1)
