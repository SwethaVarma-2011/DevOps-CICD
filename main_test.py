import unittest
from flask import Flask, send_from_directory

app = Flask(__name__)

expected = "text/html; charset=utf-8" 

@app.route('/home')
def home_page():
    return send_from_directory('static', 'home.html')

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
        # Just verify the code not html content
        self.assertEqual(response.content_type, expected)

    def test_course_page(self):
        response = self.app.get('/courses')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, expected)

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, expected)

    def test_contact_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, expected)
    

if __name__ == '__main__':
    unittest.main()
