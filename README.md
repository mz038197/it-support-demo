# it-support-demo

IT 部門的小工具專案。這是「AI Agent 企業流程整合進階工作坊」第一天使用的示範 repo。

## 內容

| 模組 | 功能 |
|---|---|
| `it_tools/password.py` | 檢查密碼是否符合公司規則 |
| `it_tools/vpn.py` | 檢查 VPN 設定檔 |
| `it_tools/disk.py` | 計算磁碟用量 |

## 工作規則

- 每個修改都對應一張 Jira 工單，專案金鑰是 `SUP`。
- 分支名稱用工單編號開頭，例如 `SUP-3-fix-vpn-timeout`。
- 開 PR 時，GitHub Actions 會自動執行 `pytest`。

## 給學員

這個 repo 是範本。請按右上角的 **Use this template**，在自己的帳號建立一份。
接著執行課程資料夾的 `setup/seed_github.py`，建立示範用的 PR。
