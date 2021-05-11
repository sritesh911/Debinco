from flask import Flask
from flask import render_template


app = Flask(__name__)
FLASK_ENV = "development"

@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)


if __name__ == '__main__':
    app.run()
