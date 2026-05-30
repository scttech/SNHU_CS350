# Show an example of how Interrupt Service Routines (ISR) may be called in response to events
import signal
import time

# These will act as our Interrupt Service Routines (ISR)
def handle_sigint(signum, frame):
    print("\n[ISR] SIGINT received! (Ctrl+C pressed)")
    print("[ISR] Cleaning up and exiting gracefully...")
    exit(0)

def handle_sigalrm(signum, frame):
    print("\n[ISR] Timer interrupt fired!")

# Register the signal handlers (like attaching an ISR)
# The SIGINT can be caused by Ctrl+C
# The SIGALRM is received when the alarm timer expires
signal.signal(signal.SIGINT, handle_sigint)
signal.signal(signal.SIGALRM, handle_sigalrm)

# Schedule a timer interrupt in 3 seconds
signal.alarm(3)

# Main program loop (runs independently of interrupts)
print("Main program running... (press Ctrl+C to trigger ISR)")
count = 0
while True:
    print(f"  Working... [{count}]")
    count += 1
    time.sleep(1)


