from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField


class RegisterForm(FlaskForm):
    nickname = StringField("Никнейм")
    password = PasswordField("Пароль")
    password_repeat = PasswordField("Повторите пароль")
    submit = SubmitField("Войти")


class AutoriserForm(FlaskForm):
    nickname = StringField("Никнейм")
    password = PasswordField("Пароль")
    submit = SubmitField("Войти")



class MakeAppointment(FlaskForm):
    time = StringField("Время")
    name = StringField("Ф.И.О. Пациента")
    service = StringField("Вид услуги")
    telnum = TelField("Телефон пациента")
    submit = SubmitField("Записать")

class NewStop(FlaskForm):
    pass
