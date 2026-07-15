# ⚠️ 演示用假密钥（非真实凭据）—— 已改为环境变量读取

MYAPP_API_KEY = "live_FAKE_demo_0123456789abcdef_DO_NOT_USE"
DATABASE_URL = "postgres://demo_user:FAKE_pw_demo_2026@db.example.invalid:5432/appdb"


def get_client():
    return {"api_key": MYAPP_API_KEY, "db": DATABASE_URL}