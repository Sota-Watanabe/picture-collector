from flask import Flask, request
app = Flask(__name__)
 
 
@app.route("/post", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        hoge = request.form['foo']
        return hoge
    else:
        hoge = request.form['foo']
        return hoge   
 
if __name__ == '__main__':
    # http://localhost:5000/ でアクセスできるよう起動
    app.run(host='localhost', port=5000)