from flask import Flask, current_app, make_response, redirect, abort, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', url_for=url_for)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<int:id>')
def user_id(id):
    return '<h1>Hello %d!</h1>' % id


@app.route('/bad')
def bad_request():
    return ('<h1>Bad Request</h1>', 400, {'Content-Type': 'text/json'})

@app.route('/not_found')
def not_found():
    res = make_response('<h1>not found</h1>', 404)
    # 第二个参数必须是字符串
    res.set_cookie('answer', '42')
    return res

@app.route('/redirect')
def redirect_kjl():
    res = redirect('http://www.kujiale.com')
    return res

@app.route('/error/<id>')
def error(id):
    if not id:
        abort(404)
    return 'This is not Error'

if __name__ == '__main__':
    app.run(debug=True)