import os
import base64
import codecs
import subprocess
from datetime import datetime
from flask import Flask, request
import server_setting

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! This is sotaServer in SIT !"

@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        enc_img = request.form['enc_img']
        ex = request.form['extension']
        content = base64.b64decode(enc_img)
        time = datetime.now().strftime("%Y%m%d-%H%M%S")
        try:
            os.makedirs(server_setting.SAVE_PATH, exist_ok=True)
            with codecs.open(server_setting.SAVE_PATH + time + ex, 'wb') as fo:
                fo.write(content)
        
            subprocess.run("sudo pkill -9 -x fbi".split())
            subprocess.run("sudo fbi -T 1 -a -noverbose -t 30 -u -blend 4000 /home/pi/Pictures/img_from_bot/*", shell=True)


        except PermissionError as ex:
            return 'サーバ側でエラーが発生しました。\n開発者に連絡してください\n' + ex
        except subprocess.SubprocessError as ex:
            return 'サーバ側でエラーが発生しました。\n開発者に連絡してください\n' + ex

        return 'uploadが完了しました!'


    else:
        return 'GET'


if __name__ == '__main__':
    # flaskのデフォルトポートは5000番
    app.run(host=server_setting.SAVE_SERVER_IP)
    # 外部とつなげる場合はポートを80に設定する
    # app.run(host=server_setting.SAVE_SERVER_IP, port=80)