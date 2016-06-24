from flask import Flask,make_response
import os

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'planup.db'),
    DEBUG=True,
    SECRET_KEY='developmentkey',
    USERNAME='admin',
    PASSWORD='default',
    VERSION='0.0.1'))

@app.route('/version')
def version():
    response = make_response('{"version" : %s }' % app.config.get('VERSION'), 200)
    response.content_type = "application/json"
    return response
