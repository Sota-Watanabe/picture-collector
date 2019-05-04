
API_TOKEN = 'xxxxxxxxxxxxx-slackbotのトークン-xxxxxxxxxxxxx'


# デフォルトの応答
DEFAULT_REPLY = 'こんにちは、ピクコレです！\n好きな画像をみんなでコレクションしましょう！\n\
uploadというメッセージに画像を添付すると画像がアップロードされます！'

SAVE_SERVER_URL = 'http://127.0.0.1:5000/post'

# 外部とつなげる場合はポート指定なし(80番につながる)
# SAVE_SERVER_URL = 'http://xxx.xxx.xxx.xxx/post'

PLUGINS = ['botmodules.conversation']