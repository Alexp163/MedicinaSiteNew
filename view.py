from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Ivan'
    return render_template('single.html', n=name)

@app.route('/select_action')
def select_action():
    return render_template('selection_page.html')