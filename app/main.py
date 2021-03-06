from flask import Flask, request, make_response
from utils.calendar import makeICS

app = Flask(__name__)


@app.route('/ics')
def manyUser():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        # (username)
        x = makeICS(username, password)
        resp = make_response(x)
        resp.headers['Content-Type'] = "text/calendar;charset=UTF-8"

        if x:
            return resp
        else:
            return '学号不存在或者密码错误.'
    except:
        return '学号不存在或者密码错误'


@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-91727260-3', 'auto');
  ga('send', 'pageview');

</script>
    <title>获取日历事件</title>
</head>

<body>
    <form action="/ics" ,method="get">
        学号<input type="text" name="username" id="username">
        <hr> 密码
        <input type="text" name="password" id="password">
        <hr>
        <input type="submit" value="get">
    </form>
    <hr>
    <p>ios用户<b>请用safari打开本网页</b>在输入学号密码之后将事件添加到日历
hotmail,outlook或者谷歌日历用户使用相应的web客户端订阅打开的链接.</p>
<hr>
    <a href="https://github.com/trim21/sdu2ics">项目主页</a>
</body>

</html>"""


@app.route('/exam')
def manyUser():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        # (username)
        x = makeICS(username, password)
        resp = make_response(x)
        resp.headers['Content-Type'] = "text/calendar;charset=UTF-8"

        if x:
            return resp
        else:
            return '学号不存在或者密码错误.'
    except:
        return '学号不存在或者密码错误'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=800)
