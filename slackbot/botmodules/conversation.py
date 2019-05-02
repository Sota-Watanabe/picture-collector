import codecs
import base64
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
        url = message.body['files'][0]['url_private']
        try:
            content = requests.get(
                url,
                allow_redirects=True,
                headers={'Authorization': 'Bearer %s' % slackbot_settings.API_TOKEN}, stream=True
            ).content
            enc_file = base64.b64encode(content)
            url = slackbot_settings.SAVE_SERVER_URL
            payload = {'enc_img': enc_file}
            response = requests.post(url, payload)
            print(response.text)
            message.reply('upload完了')
        except requests.ConnectionError as ex:
            message.reply('エラーが発生しました。\n画像保存サーバが機能しているか確かめてください\n'
                          + str(ex))
    else:
        message.reply('画像を添付してください')
























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