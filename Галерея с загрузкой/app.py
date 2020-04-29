import os

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    title = 'Мои достижения'
    pictures = os.listdir('static/img')
    if request.method == 'GET':
        return render_template('galery.html', pictures=pictures, title=title)
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{len(pictures) + 1}.jpg', 'wb') as file:
            file.write(f.read())
        print(request)
        return "Добавить"


if __name__ == '__main__':
    app.run(port=80, host='127.0.0.1')
