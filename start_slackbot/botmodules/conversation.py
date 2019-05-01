from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import slackbot_settings
import codecs
import requests
import base64

# メンションあり応答
@respond_to('こんにちは')
def greeting(message):
    # メンションして応答
    message.reply('こんにちは!')

@default_reply
def my_default_handler(message):
    # デフォルトリプライをsendに変更する
    message.send(slackbot_settings.DEFAULT_REPLY)


@respond_to('upload')
def greeting1(message):
    # メンションして応答
    url = message.body['files'][0]['url_private']

    # rst = requests.get(url, headers={'Authorization': 'Bearer %s' % slackbot_settings.API_TOKEN}, stream=True)
    content = requests.get(
        url,
        allow_redirects=True,
        headers={'Authorization': 'Bearer %s' % slackbot_settings.API_TOKEN}, stream=True
    ).content

    enc_file = base64.b64encode(content)
    url = 'http://127.0.0.1:5000/post'
    payload = {'enc_img': enc_file}
    response = requests.post(url, payload)
    print(response.text)
    message.reply('upload完了')

























# @respond_to('^ファイルダウンロード$')
@respond_to('^アップロード$')
def file_download(message):
    # ダウンロードするファイルタイプを指定する
    file_types = ['png', 'jpg']
    # ファイルの保存ディレクトリ
    save_path = '/home/sota/Desktop/'

    download_file = DownloadFile(file_types, save_path)
    result = download_file.exe_download(message._body['files'][0])

    if result == 'ok':
        message.send('ファイルがスライドショーに追加されました (仮)')
    elif result == 'file type is not applicable.':
        message.send('ファイルのタイプがダウンロード対象外です')
    else:
        message.send('失敗しました')


class DownloadFile:
    def __init__(self, file_types, save_directly):
        # 引数が省略された場合は、デフォルトのタイプを指定
        self.file_types = file_types
        self.save_directly = save_directly

    def exe_download(self, file_info):

        file_name = file_info['name']
        url_private = file_info['url_private_download']

        # 保存対象のファイルかチェックする
        if file_info['filetype'] in self.file_types:
            # ファイルをダウンロード
            self.file_download(url_private, self.save_directly + file_name)
            return 'ok'
        else:
            # 保存対象外ファイル
            return 'file type is not applicable.'

    def file_download(self, download_url, save_path):
        content = requests.get(
            download_url,
            allow_redirects=True,
            headers={'Authorization': 'Bearer %s' % slackbot_settings.API_TOKEN}, stream=True
        ).content
        # 保存する
        target_file = codecs.open(save_path, 'wb')
        target_file.write(content)
        target_file.close()