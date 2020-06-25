from tests.base import BaseTestCase


class TestBasic(BaseTestCase):

    def test_basic(self):
        response = self.client.post('/api/auth/login', json={"username": "test", "password": "Admin@1234"})
        self.assertEqual(response.status_code, 200)

    def test_basic1(self):
        response = self.client.post('/api/auth/login', json={"username": "test", "password": "Admin@1234"})
        self.assertEqual(response.status_code, 200)