from flask import Flask
from controller.TemperatureController import temperatureBlueprint

app = Flask(__name__)
app.register_blueprint(temperatureBlueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')