from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    nickname = StringField("Никнейм")
    password = PasswordField("Пароль")
    password_repeat = PasswordField("Повторите пароль")
    submit = SubmitField("Войти")


class AutoriserForm(FlaskForm):
    nickname = StringField("Никнейм")
    password = PasswordField("Пароль")
    submit = SubmitField("Войти")
