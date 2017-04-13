from flask import Flask, request
from .utils.calendar import makeiCs

app = Flask(__name__)


@app.route('/ics')
def manyUser():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        x = makeiCs(username, password)
        if x:
            return x
        else:
            return '密码错误'
    except:
        return 'url错误'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=800)