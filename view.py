from app import app
from flask import render_template
from forms import RegisterForm, AutoriserForm

doctors = {
    'karsonov': 'Карсонов Максим Петрович',
    'jigunova': 'Жигунова Карина Аркадьевна',
    'sapeturov': 'Сапетуров Борис Игнатьевич',
    'kuznetsov': 'Кузнецов Виктор Сергеевич',
    'sokolova': 'Соколова Алина Владимировна',
    'zapolskyi': 'Запольский Семен Рудольфович'
}

doctors_times = {
    'karsonov': ["08:00", "09:30",  "10:30", ],
    'jigunova': ["10:00", "10:30", "11:00"],
    'sapeturov': ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30"],
    'kuznetsov': ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30"],
    'sokolova': ["08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00"],
    'zapolskyi': ["10:00", "10:30"],
}

times = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30"]


users = {
    "admin": "qwerty12345",
    "user": "q12345"
}


@app.route('/')
def index():
    name = 'Ivan'
    return render_template('single.html', n=name)

@app.route('/consultation/<string:surname>')
def karsonov_consultation(surname):
    if surname not in doctors:
        return "Врач не найден"

    fio = doctors[surname]
    free_hours = doctors_times[surname]

    return render_template('doctor_page.html', name_surname=fio, times=times,free_hours=free_hours)


@app.route('/select_action')
def select_action():
    return render_template('selection_page.html')


@app.route('/admin_select')
def admin_select():
    return render_template('admin_select.html')


@app.route('/autorization_user', methods=["GET", "POST"])
def autorization_user():
    autorizer_form = AutoriserForm()

    if autorizer_form.validate_on_submit():
        print("Данные введены: ")
        print(autorizer_form.nickname.data)
        print(autorizer_form.password.data)

        if autorizer_form.nickname.data in users and autorizer_form.password.data == users.get(autorizer_form.nickname.data):
            return "Пользователь авторизован!"
        else:
            return "Логин или пароль не корректны!"

    return render_template('authorization.html', form=autorizer_form)





@app.route('/registration_user', methods=["GET", "POST"])
def registration_user():
    form = RegisterForm()

    if form.validate_on_submit():
        print("Данные пришли: ")
        print(form.nickname.data)
        print(form.nickname.data)
        print(form.password.data)
        print(form.password_repeat.data)

        if form.password.data == form.password_repeat.data:
            users[form.nickname.data] = form.password.data
            return "Проверьте почту и подтвердите регистрацию"
        else:
            return "Пароли не совпадают!"

    return render_template('registration.html', form=form)


@app.route('/patient_data')
def patient_data():
    return render_template('patient_data.html')


@app.route('/selection_page')
def selection_page():
    return render_template('selection_page.html')
