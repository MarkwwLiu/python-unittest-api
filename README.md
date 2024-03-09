# python-unittest-api

這個資料夾是用於存放 API 測試相關的程式碼和測試用例。以下是資料夾內容的詳細說明：

### 文件結構

```
api_test/
│
├── config/
│   └── domain.py           # 定義了測試用的網域字典
│
├── report/                 # 存放測試報告的資料夾
│
├── src/
│   └── common/
│       └── HTMLTestRunner_PY3.py    # 自定義的 HTMLTestRunner 模組
│
├── test_cases/             # 存放測試用例的資料夾
│   ├── __init__.py
│   └── web_checkout_status_code_test_cases.py  # 測試用例
│
└── README.md               # 說明文件，本檔案
```

### 域名設定

在 `config/domain.py` 檔案中，定義了測試所需的網域字典，包括了三個網站的 URL：

- `share_web`: https://shareboxnow.com/
- `google_web`: https://www.google.com.tw/
- `yahoo_web`: https://tw.yahoo.com/

### 測試用例

測試用例存放在 `test_cases/` 資料夾中，每個測試用例檔案都包含了對應網站的測試。在 `test_cases/` 資料夾中，您可以找到以下檔案：

- `web_checkout_status_code_test_cases.py`: 測試 `share_web`, `google_web`, `yahoo_web` 的測試用例

### 報告

測試報告將保存在 `report/` 資料夾中，每次執行測試後將生成一份新的 HTML 報告。

### 自定義模組

在 `src/common/HTMLTestRunner_PY3.py` 檔案中，提供了一個自定義的 HTMLTestRunner 模組，用於生成美觀的 HTML 測試報告。
