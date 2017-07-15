class Temperature:

    # constructor with an attribute called temperature.
    # When instance = Temperature('30') then instance.temperature is '30'
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity