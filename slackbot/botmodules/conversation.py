import codecs
import base64
import os
import requests
from slackbot.bot import respond_to
from slackbot.bot import default_reply
import slackbot_settings


@default_reply
def my_default_handler(message):
    if 'files' in message.body:
        message.reply('"upload"というメッセージに画像を添付してください')
    else:
        message.reply(slackbot_settings.DEFAULT_REPLY)


@respond_to('^upload$')
def upload(message):
    if 'files' in message.body:
        message.reply('upload中...')
        url = message.body['files'][0]['url_private']
        ex = os.path.splitext(url)[1]
        try:
            content = requests.get(
                url,
                allow_redirects=True,
                headers={'Authorization': 'Bearer %s' % slackbot_settings.API_TOKEN}, stream=True
            ).content
            enc_file = base64.b64encode(content)
            url = slackbot_settings.SAVE_SERVER_URL
            payload = {'enc_img': enc_file, 'extension': ex}
            response = requests.post(url, payload)
            reply_msg = response.text
        except requests.ConnectionError as ex:
            reply_msg = 'slackbot側でエラーが発生しました。\n開発者に連絡してください\n' + str(ex)
    else:
        reply_msg = '画像を添付してください'

    message.reply(reply_msg)
