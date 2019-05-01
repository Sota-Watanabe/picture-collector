from flask import Flask, request
import requests, urllib3, os, shutil, base64, codecs
import server_setting
app = Flask(__name__)

 
@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        enc_img = request.form['enc_img']
        content = base64.b64decode(enc_img)

        with codecs.open(server_setting.SAVE_PATH + request.form['name'], 'wb') as fo:
            fo.write(content)
        

        return 'aaa'
    else:
        hoge = request.form['foo']
        return 'GET'   
 

if __name__ == '__main__':
    # http://localhost:5000/ でアクセスできるよう起動
    app.run(host='localhost', port=5000)