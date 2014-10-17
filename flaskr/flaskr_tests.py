# -*- coding:utf-8 -*-
import os
import flaskr
import unittest
import tempfile


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, passwd):
        return self.app.post('/login/', data=dict(
            username=username, password=passwd),
            follow_redirects=True)

    def logout(self):
        return self.app.get('/logout/', follow_redirects=True)

    def test_loginout(self):
        rv = self.login('admin', 'passwd')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You have logged out' in rv.data
        rv = self.login('adminx', 'passwd')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    def test_message(self):
        self.login('admin', 'passwd')
        rv = self.app.post('/add/', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
            ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data


if __name__ == '__main__':
    unittest.main()
