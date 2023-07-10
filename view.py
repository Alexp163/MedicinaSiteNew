from app import app
from flask import render_template
from app import Users, Profiles


@app.route('/')
def index():
    name = 'Ivan'
    print(Users.query.all())
    print(Profiles.query.all())

    return render_template('single.html', n=name)


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


@app.route('/karloson_consultation')
def karsonov_consultation():
    return render_template('karsonov.html')


@app.route('/jigunova_consultation')
def jigun_consultation():
    return render_template('jigunova.html')


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



