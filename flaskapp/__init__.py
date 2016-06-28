"""
    PlanUp

    An application which helps users planning movies,
    outings,trips with their friends.
"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask,make_response,g
import os,json

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'planup.db'),
    DEBUG=True,
    SECRET_KEY='developmentkey',
    USERNAME='admin',
    PASSWORD='default',
    VERSION='0.0.1'))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def return_response(response_dict, code=200):
    response = make_response(json.dumps(response_dict))
    response.content_type = "application/json"
    return response, code

@app.route('/init_db')
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    resp = {"message":"Data Initialized"}
    return return_response(resp)


def get_db():
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.route('/version')
def version():
    response = make_response('{"version" : %s }' % app.config.get('VERSION'), 200)
    response.content_type = "application/json"
    return response

@app.route('/add_user',methods=['POST'])
def add_user():
    print request.json
