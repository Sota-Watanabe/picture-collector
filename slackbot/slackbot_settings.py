# ライブラリのインポート
import os

# 環境変数に定義しておく
API_TOKEN = 'xoxb-46717260934-622020920560-manGX2nOhL2yKRmcxaA4EYkk'

# デフォルトの応答
DEFAULT_REPLY = "すみません。よくわかりません"

PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]
