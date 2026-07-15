import os

# ⚠️ 演示用假密钥（非真实凭据）—— 已改为环境变量读取

MYAPP_API_KEY = os.environ.get("MYAPP_API_KEY", "your_api_key_here")
DATABASE_URL = os.environ.get("DATABASE_URL", "your_database_url_here")


def get_client():
    return {"api_key": MYAPP_API_KEY, "db": DATABASE_URL}