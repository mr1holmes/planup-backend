"""
    Tests Planup Application
"""

import pytest
import os
import flaskapp
import tempfile

@pytest.fixture
def client(request):
    db_fd, flaskapp.app.config['DATABASE'] = tempfile.mkstemp()
    flaskapp.app.config['TESTING'] = True
    client = flaskapp.app.test_client()
    with flaskapp.app.app_context():
        flaskapp.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(flaskapp.app.config['DATABASE'])
    
    request.addfinalizer(teardown)
    return client

# Example test
def test_version(client):
    resp = client.get('/version', follow_redirects=True)
    print type(resp)
    assert b''+flaskapp.app.config['VERSION'] in resp.data
