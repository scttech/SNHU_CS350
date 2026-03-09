# A simple Raspberry Pi program to ensure the LED is working
import sys
import time

import RPi.GPIO as GPIO

GREEN_LED_PIN = 18
RED_LED_PIN = 23
YELLOW_LED_PIN = 24

LED_MAP = {
    "GREEN": GREEN_LED_PIN,
    "RED": RED_LED_PIN,
    "YELLOW": YELLOW_LED_PIN,
}

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python led_tester.py [GREEN|RED|YELLOW]")
        sys.exit(1)

    color = sys.argv[1].upper()
    if color not in LED_MAP:
        print("Invalid color. Use GREEN, RED, or YELLOW.")
        sys.exit(1)

    pin = LED_MAP[color]

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
    GPIO.setup(RED_LED_PIN, GPIO.OUT)
    GPIO.setup(YELLOW_LED_PIN, GPIO.OUT)

    try:
        # Turn all off first
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_LED_PIN, GPIO.LOW)

        # Turn requested LED on
        GPIO.output(pin, GPIO.HIGH)
        print(f"{color} LED ON (pin {pin}). Press Ctrl+C to exit.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("\nClean exit.")


if __name__ == "__main__":
    main()


