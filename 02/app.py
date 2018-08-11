from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

@app.route('/user/<int:id>')
def userid(id):
    return '<h1>Hello %d!</h1>' % id

if __name__ == '__main__':
    app.run(debug=True)