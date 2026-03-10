import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

try:
    print("---------- GPIO18 HIGH ----------")
    GPIO.output(18, GPIO.HIGH)
    os.system("gpio readall")
    time.sleep(2)

    print("---------- GPIO18 LOW ----------")
    GPIO.output(18, GPIO.LOW)
    os.system("gpio readall")
    time.sleep(2)
finally:
    GPIO.cleanup()

print("GPIO cleanup done, check pins again")

os.system("gpio readall")