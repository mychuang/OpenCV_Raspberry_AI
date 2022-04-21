import time, RPi.GPIO as GPIO

pingID = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pingID, GPIO.OUT)

try:
    while True:
        GPIO.output(pingID, 1) #open LED
        time.sleep(1)
        GPIO.output(pingID, 0) #close LED
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.output(pingID, 0) #close LED