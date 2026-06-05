# A simple Raspberry Pi program to ensure the pin is on/off.  Combine this script with an LED to help verify wiring,
# breadboard, cables, are all setup correctly
import sys
import time

import RPi.GPIO as GPIO

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python pin_tester.py [pin]")
        sys.exit(1)

    try:
        pin = int(sys.argv[1])
    except ValueError:
        print("Error: pin must be an integer")
        sys.exit(1)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    try:
        # Turn requested pin off
        GPIO.output(pin, GPIO.LOW)

        # Turn requested pin on
        GPIO.output(pin, GPIO.HIGH)
        print(f"ON (pin {pin}). Press Ctrl+C to exit.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("\nClean exit.")


if __name__ == "__main__":
    main()


