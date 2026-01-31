# This imports the Python serial package to handle communications over the
# Raspberry Pi's serial port.
import serial

# Import the time package to allow us to add delays
import time

# Load the GPIO interface from the Raspberry Pi Python Module
# The GPIO interface will be available through the GPIO object
import RPi.GPIO as GPIO

ser = serial.Serial(
        port='/dev/ttyS0', # This command assumes that we are using the Raspberry
                           # Pi's onboard serial port located at /dev/ttyS0.
        baudrate = 115200, # This sets the speed of the serial interface in
                           # bits/second
        parity=serial.PARITY_NONE,      # Disable parity
        stopbits=serial.STOPBITS_ONE,   # Serial protocol will use one stop bit
        bytesize=serial.EIGHTBITS,      # We are using 8-bit bytes
        timeout=1          # Configure a 1-second timeout
)

PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

# Configure our loop variable
repeat = True

# Loop until the user hits CTRL-C or the client sends an exit/quit message

# Read lines from the serial port 1 at a time.
# This will block until we have data available.
try:
    while repeat:
        # Read a line from the serial port.
        command = ((ser.readline()).decode("utf-8")).lower()

        # The underscore symbol '_' is used to represent the default case
        # if nothing else matches in our list of cases.
        match command:
            case "blink":
                GPIO.output(PIN, True)
                time.sleep(0.5)
                GPIO.output(PIN, False)
                time.sleep(0.5)

            case "quit":
               repeat = False
               print("Exiting LED server")

            case _:
                # No valid commands in the input so do nothing
                pass

except KeyboardInterrupt:
    pass
finally:
    GPIO.output(PIN, False)
    GPIO.cleanup()
