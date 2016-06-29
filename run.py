import flaskapp
from flaskapp import app

if __name__ == "__main__":
    #initialize the database before starting the application
    with app.app_context():
        flaskapp.init_db()
    app.run()
