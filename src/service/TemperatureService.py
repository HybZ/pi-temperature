from repository.RaspberrypiRepository import raspberrypiRepository

class TemperatureService:

    def currentTemperature(self):
        return raspberrypiRepository.readTemperature()

temperatureService = TemperatureService()