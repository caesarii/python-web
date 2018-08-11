from flask import Flask
from flask import current_app
app = Flask(__name__)
# 获取程序上下文
app_ctx = app.app_context()
# 推送上下文
app_ctx.push()
@app.route('/')
def index():
    print('当前程序实例', current_app.name)
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

@app.route('/user/<int:id>')
def user_id(id):
    return '<h1>Hello %d!</h1>' % id


@app.route('/bad')
def bad_request():
    return ('<h1>Bad Request</h1>', 400, {'Content-Type': 'text/json'})
if __name__ == '__main__':
    app.run(debug=True)