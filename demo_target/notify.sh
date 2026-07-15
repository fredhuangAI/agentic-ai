#!/usr/bin/env bash
# ⚠️ 演示用假 webhook（非真实）—— 从环境变量读取

FEISHU_WEBHOOK="https://open.feishu.cn/open-apis/bot/v2/hook/FAKE-0000-demo-do-not-use"
curl -s -X POST "$FEISHU_WEBHOOK" -d '{"msg":"demo"}'