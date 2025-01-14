import unittest
from app import create_app, db
from app.users.models import User

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name = "test_config")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    def test_register_page_loads(self):
        response = self.client.get('/user/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'register', response.data)

    def test_login_page_loads(self):
        response = self.client.get('/user/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'login', response.data)

    def test_user_registration(self):
        response = self.client.post('/user/register', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        }, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.email, 'testuser@example.com')

    def test_user_login(self):
        with self.app.app_context():
            user = User(username='testuser', email='testuser@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/user/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_user_logout(self):
        with self.app.app_context():
            user = User(username='testuser', email='testuser@example.com', password='testpassword')
            db.session.add(user)
            db.session.commit()

        self.client.post('/user/login', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.get('/user/logout')
        self.assertEqual(response.status_code, 302)

    if __name__ == "__main__":
        unittest.main()