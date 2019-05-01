import pprint
import requests

def main():
    #POSTパラメータは二つ目の引数に辞書で指定する
    response = requests.post(
        'http://127.0.0.1:5000/post',
        {'foo':'bar'})
    #レスポンスオブジェクトのjsonメソッドを使うと、
    #JSONデータをPythonの辞書オブジェクトに変換して取得できる
    print(response)
    print(response.url)
    print(response.headers)
    print(response.text)
if __name__=='__main__':
    main()

