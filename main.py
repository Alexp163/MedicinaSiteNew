from app import app, db
import view


if __name__ == '__main__':
    from view import app
    with app.app_context():
        db.create_all()
    app.run(debug=True)
