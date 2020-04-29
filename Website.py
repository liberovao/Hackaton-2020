from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')