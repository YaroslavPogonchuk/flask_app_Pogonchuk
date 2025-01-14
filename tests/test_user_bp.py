import unittest
from app import app # Переконайтеся, що імпортували ваш Flask-додаток

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Налаштування клієнта тестування перед кожним тестом."""
        app.config["TESTING"] = True
        self.client = app.test_client()
    def test_greetings_page(self):
        """Тест маршруту /hi/<name>."""
        response = self.client.get("/users/hi/John?age=30")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome John", response.data)
        self.assertIn(b"age: 30", response.data)
    def test_admin_page(self):
        """Тест маршруту /admin, який перенаправляє."""
        response = self.client.get("/users/admin", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome Admin", response.data)
        self.assertIn(b"age: 22", response.data)

if __name__ == "__main__":
    unittest.main()