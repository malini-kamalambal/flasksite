from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import form

app = Flask(__name__)


@app.route('/')
def index():
    return 'Test Flask Site'


@app.route('/hello/')
def hello():
    return 'halo halo'


@app.route('/hello/<user_name>/')
def hello_user(user_name):
    return render_template('hello.html', name=user_name)


@app.route('/hello/<user_name>/upload/', methods=['GET', 'POST'])
def upload_file(user_name):
    if request.method == 'POST':
        form.photo.data.save('/var/www/uploads/{0}.jpg'.format(user_name))
    else:
        return render_template('gorilla.html', name=user_name)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
