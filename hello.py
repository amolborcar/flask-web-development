from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return redirect('http://www.example.com')

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello %s! </h1>' % name

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s!</h1>' % user.name

if __name__ == '__main__':
    manager.run()