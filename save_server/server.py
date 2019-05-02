import os
import base64
import codecs
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
        if not os.path.isfile(server_setting.SAVE_PATH):
            os.makedirs(server_setting.SAVE_PATH)
        with codecs.open(server_setting.SAVE_PATH + time + ex, 'wb') as fo:
            fo.write(content)
        return 'OK'
    else:
        return 'GET'


if __name__ == '__main__':
    # app.run(debug=False, host='0.0.0.0', port=80)
    app.run(host="0.0.0.0", port=80)
