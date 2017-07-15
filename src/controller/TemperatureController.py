from flask import Blueprint, render_template
from service.TemperatureService import temperatureService

temperatureBlueprint = Blueprint('temperatureController', __name__, template_folder='../../templates')

@temperatureBlueprint.route('/temperature')
def temperature():
    currentTemperature = temperatureService.currentTemperature()
    return render_template('temperature.xhtml', temperature = currentTemperature.temperature, humidity = currentTemperature.humidity)