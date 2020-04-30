from flask import Flask, url_for, request, render_template
from data import db_session
from data.register import RegisterForm
from data.users import User
import os

app = Flask(__name__)


def main():
    db_session.global_init("db/users_info.sqlite")

    @app.route('/')
    def reactive_str():
        return render_template('base.html')
   

    @app.route('/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация', form=form,
                                       message="Пароли не совпадают")
            session = db_session.create_session()
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация', form=form,
                                       message="Такой пользователь уже есть")
            user = User(
                name=form.name.data,
                email=form.email.data,
                about=form.about.data
            )
            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)


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