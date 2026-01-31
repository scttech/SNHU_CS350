# A simple Raspberry Pi program to control an LED's brightness and blink frequency
# using PWM on a GPIO pin. The user can adjust the frequency and duty cycle with the arrow keys
import sys
import time
import select
import termios
import tty
import os

import RPi.GPIO as GPIO

PIN = 18

FREQ_MIN, FREQ_MAX = 1, 5000
FREQ_STEP = 1

DUTY_MIN, DUTY_MAX = 0, 100
DUTY_STEP = 5

# Loop delay
TICK = 0.02 

def clamp(n, low, high):
    """
    Ensure the value is between two numbers
    """
    if n < low:
        return low
    elif n > high:
        return high
    else:
        return n

def drain_stdin_bytes():
    """
    Read and return all currently-available bytes from 
    stdin (non-blocking via select).
    """
    data = b""
    while select.select([sys.stdin], [], [], 0)[0]:
        chunk = os.read(sys.stdin.fileno(), 1024)
        if not chunk:
            break
        data += chunk
        # If less than buffer size, we've probably drained it
        if len(chunk) < 1024:
            break
    return data

def parse_keys_from_buffer(buf: bytes):
    """
    Consume as many complete key events as possible from buf.
    Returns (events, remaining_buf).
    events contains: 'UP','DOWN','LEFT','RIGHT','q','Q', etc.
    """
    key_presses = []
    i = 0
    n = len(buf)

    while i < n:
        b = buf[i:i+1]

        # Arrow key escape sequences: ESC [ A/B/C/D
        if b == b"\x1b":
            if i + 2 < n and buf[i+1:i+2] == b"[":
                code = buf[i+2:i+3]
                mapping = {b"A": "UP", b"B": "DOWN", b"C": "RIGHT", b"D": "LEFT"}
                evt = mapping.get(code)
                if evt:
                    key_presses.append(evt)
                    i += 3
                    continue
            # Incomplete ESC sequence -> wait for more bytes next loop
            break

        # Regular single-byte chars (e.g. 'q', 'Q')
        ch = b.decode("utf-8", errors="ignore")
        if ch:
            key_presses.append(ch)
        i += 1

    return key_presses, buf[i:]


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

freq = 60
duty = 50

pwm = GPIO.PWM(PIN, freq)
pwm.start(duty)

fd = sys.stdin.fileno()
old_term = termios.tcgetattr(fd)

print("Arrow keys: LEFT/RIGHT = frequency, UP/DOWN = duty. Press 'q' to quit.")

input_buf = b""
last_print = 0.0

try:
    # Set single key input
    tty.setraw(fd)

    while True:
        # Read everything that has arrived since last tick, append to buffer
        input_buf += drain_stdin_bytes()

        # Parse as many key events as we can
        events, input_buf = parse_keys_from_buffer(input_buf)

        for key in events:
            if key == "RIGHT":
                freq = clamp(freq + FREQ_STEP, FREQ_MIN, FREQ_MAX)
                pwm.ChangeFrequency(freq)
            elif key == "LEFT":
                freq = clamp(freq - FREQ_STEP, FREQ_MIN, FREQ_MAX)
                pwm.ChangeFrequency(freq)
            elif key == "UP":
                duty = clamp(duty + DUTY_STEP, DUTY_MIN, DUTY_MAX)
                pwm.ChangeDutyCycle(duty)
            elif key == "DOWN":
                duty = clamp(duty - DUTY_STEP, DUTY_MIN, DUTY_MAX)
                pwm.ChangeDutyCycle(duty)
            elif key in ("q", "Q"):
                raise KeyboardInterrupt

        # Update status
        now = time.time()
        if now - last_print > 0.05:
            sys.stdout.write(f"\rFreq: {freq:4d} Hz | Duty: {duty:3d}%   (q to quit)   ")
            sys.stdout.flush()
            last_print = now

        time.sleep(TICK)
except KeyboardInterrupt:
    pass
finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_term)
    pwm.stop()
    GPIO.cleanup()
    print("\nClean exit.")

