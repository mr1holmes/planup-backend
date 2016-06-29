"""
    PlanUp

    An application which helps users planning movies,
    outings,trips with their friends.
"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask,make_response,g,request
import os,json

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'planup.db'),
    DEBUG=True,
    SECRET_KEY='developmentkey',
    USERNAME='admin',
    PASSWORD='default',
    VERSION='0.0.1'))

def connect_db():
    """Connects to the database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print 'Database Intialized'


def get_db():
    """
    Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def return_response(response_dict, code=200):
    """Converts dictionary to flask return object"""
    response = make_response(json.dumps(response_dict))
    response.content_type = "application/json"
    return response, code


@app.route('/version')
def version():
    resp = {'version':app.config.get('VERSION')}
    return return_response(resp, 200)

@app.route('/register_user',methods=['POST'])
def register_user():
    db = get_db()
    data = request.json.get('data')
    db.execute('insert into user values(?,?,?,?,?)',[data.get('user_id'),data.get('first_name'),
        data.get('last_name'),data.get('profile_url'),data.get('fcm_token')])
    db.commit()
    resp = {"status":"Accepted"}
    return return_response(resp,202)
