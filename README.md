# pi-temperature

## Introduction
This simple Python3 application reads the temperature using a Raspberry Pi model 3 and a DHT11 module.
It uses Flask as simple web server.

## How to run:
1. connect the DHT11 module to the raspberry pi on GPIO4 (GPIO.BCM) and 3.3v and ground
1. start TemperatureApplication using : python3 TemperatureApplication.py
1. open a browser and go to localhost:5000/temperature