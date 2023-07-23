from app import app
from flask import render_template

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


@app.route('/autorization_user')
def autorization_user():
    return render_template('authorization.html')


@app.route('/registration_user')
def registration_user():
    return render_template('registration.html')


@app.route('/patient_data')
def patient_data():
    return render_template('patient_data.html')


@app.route('/selection_page')
def selection_page():
    return render_template('selection_page.html')


# @app.route('/karloson_consultation')
# def karsonov_consultation():
#     return render_template('karsonov.html')
#
#
# @app.route('/jigunova_consultation')
# def jigun_consultation():
#     return render_template('jigunova.html')


@app.route('/sapeturov_consultation')
def sapetur_consultation():
    return render_template('sapeturov.html')


@app.route('/kuznetsov_consultation')
def kuznets_consultation():
    return render_template('kuznetsov.html')


@app.route('/sokolova_consultation')
def sokolova_consultation():
    return render_template('sokolova.html')


@app.route('/zapolskyi_consultation')
def zapolskyi_consultation():
    return render_template('zapolskyi.html')

