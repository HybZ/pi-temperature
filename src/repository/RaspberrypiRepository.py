import time as time
# import an instance from another python file
import RPi.GPIO as GPIO
# import a type (Temperature)
from model.Temperature import Temperature

class RaspberrypiRepository:

    pin = 4

    STATE_INIT_PULL_DOWN = 1
    STATE_INIT_PULL_UP = 2
    STATE_DATA_FIRST_PULL_DOWN = 3
    STATE_DATA_PULL_UP = 4
    STATE_DATA_PULL_DOWN = 5

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def readTemperature(self):
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.02)
        GPIO.setup(self.pin, GPIO.IN, GPIO.PUD_UP)

        unchangedCount = 0
        last = -1
        data = []
        state = 1
        lengths = []
        currentLength = 0
        byte = 0
        bits = []
        bytes = []

        while True:
            redInput = GPIO.input(self.pin)
            data.append(redInput)
            if last != redInput:
                unchangedCount = 0
                last = redInput
            else:
                unchangedCount += 1
                if unchangedCount > 100:
                    break

        for value in data:
            currentLength += 1

            if state == self.STATE_INIT_PULL_DOWN:
                if value == GPIO.LOW:
                    state = self.STATE_INIT_PULL_UP
                else:
                    continue
            if state == self.STATE_INIT_PULL_UP:
                if value == GPIO.HIGH:
                    state = self.STATE_DATA_FIRST_PULL_DOWN
                else:
                    continue
            if state == self.STATE_DATA_FIRST_PULL_DOWN:
                if value == GPIO.LOW:
                    state = self.STATE_DATA_PULL_UP
                else:
                    continue
            if state == self.STATE_DATA_PULL_UP:
                if value == GPIO.HIGH:
                    currentLength = 0
                    state = self.STATE_DATA_PULL_DOWN
                else:
                    continue
            if state == self.STATE_DATA_PULL_DOWN:
                if value == GPIO.LOW:
                    lengths.append(currentLength)
                    state = self.STATE_DATA_PULL_UP
                else:
                    continue
        if len(lengths) != 40:
            temperature = Temperature(temperature = 'Data not good, skip', humidity = 'Data not good, skip')
            return temperature

        shortestPullUp = min(lengths)
        longestPullUp = max(lengths)
        median = (longestPullUp + shortestPullUp) / 2
        for length in lengths:
            bit = 0
            if length > median:
                bit = 1
            bits.append(bit)
        for i in range(0, len(bits)):
            byte = byte << 1
            if bits[i]:
                byte = byte | 1
            else:
                byte = byte | 0
            if (i+1)%8 == 0:
                bytes.append(byte)
                byte = 0
        checksum = bytes[0] + bytes[1] + bytes[2] + bytes[3] & 0xFF
        if bytes[4] != checksum:
            temperature = Temperature(temperature='Data not good, skip', humidity='Data not good, skip')
            return temperature

        return Temperature(temperature = str(bytes[2]) + ',' + str(bytes[3]), humidity = str(bytes[0]) + ',' + str(bytes[1]))

    def destroy(self):
        GPIO.cleanup()

raspberrypiRepository = RaspberrypiRepository()