from flask import Flask
import sys
sys.path.append('../src')
from controller.TemperatureController import temperatureBlueprint
import unittest

class TemperatureTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(temperatureBlueprint)
        self.app = self.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/temperature')
        assert b'Temperature : Data not good, skip' in rv.data
        assert b'Humidity : Data not good, skip' in rv.data

if __name__ == '__main__':
    unittest.main()