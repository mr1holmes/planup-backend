import flaskapp
import os
from flaskapp import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    #initialize the database before starting the application
    with app.app_context():
        flaskapp.init_db()
    app.run(host='0.0.0.0',port=port)

