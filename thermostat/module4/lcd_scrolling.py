import threading
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

class LCDLineScroller:
    """
    Scrolls an arbitrary-length message across one row of a 16x2 LCD in its own thread.

    - Uses a stop Event for clean shutdown.
    - Uses a Lock so other code can safely write to the LCD if needed.
    """

    def __init__(self, lcd_write_line, cols=16, row=0, fps=5, pad=True):
        """
        lcd_write_line: callable(row:int, text:str) -> None
            Writes exactly one line (will be truncated/padded by us).
        cols: display columns (16 for a 16x2)
        row: which row to scroll on (0 or 1)
        fps: scroll updates per second (e.g., 5 feels smooth)
        pad: if True, add spacing so the message 'wraps' nicely
        """
        self._write_line = lcd_write_line
        self._cols = cols
        self._row = row
        self._delay = 1.0 / max(1, fps)
        self._pad = pad

        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread = None

        self._message = ""
        self._enabled = True

    def start(self, message: str):
        with self._lock:
            self._message = message or ""
        self._stop.clear()
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def set_message(self, message: str):
        with self._lock:
            self._message = message or ""

    def pause(self):
        self._enabled = False

    def resume(self):
        self._enabled = True

    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)

    def _run(self):
        idx = 0

        while not self._stop.is_set():
            if not self._enabled:
                time.sleep(self._delay)
                continue

            with self._lock:
                msg = self._message

            # If it fits, just show it (padded/truncated)
            if len(msg) <= self._cols:
                frame = msg.ljust(self._cols)
                self._write_line(self._row, frame)
                time.sleep(self._delay)
                continue

            # Scrolling case
            spacer = " " * self._cols if self._pad else " "
            scroll_text = msg + spacer
            # wrap-around by doubling
            doubled = scroll_text + scroll_text

            frame = doubled[idx: idx + self._cols]
            self._write_line(self._row, frame)

            idx = (idx + 1) % len(scroll_text)
            time.sleep(self._delay)


def cleanup_display(a, b, c, d, e, f):
    """
    cleanup_display - Method used to cleanup the digitalIO lines that
    are used to run the display.
    :param a: lcd_rs
    :param b: lcd_en
    :param c: lcd_d4
    :param d: lcd_d5
    :param e: lcd_d6
    :param f: lcd_d7
    :return:
    """
    # Clear the LCD first - otherwise we won't be abe to update it.
    lcd.clear()
    a.deinit()
    b.deinit()
    c.deinit()
    d.deinit()
    e.deinit()
    f.deinit()


def write_line(row: int, text: str):
    # text should be exactly 16 chars already; we enforce anyway.
    text = (text or "")[:16].ljust(16)
    lcd.cursor_position(0, row)
    lcd.message = text

# Modify this if you have a different sized character LCD
LCD_COLUMNS = 16
LCD_ROWS = 2

##
## Setup the six GPIO lines to communicate with the display.
## This leverages the digitalio class to handle digital
## outputs on the GPIO lines. There is also an analagous
## class for analog IO.
##
## You need to make sure that the port mappings match the
## physical wiring of the display interface to the
## GPIO interface.
##
## compatible with all versions of RPI as of Jan. 2019
##
lcd_rs = digitalio.DigitalInOut(board.D17)
lcd_en = digitalio.DigitalInOut(board.D27)
lcd_d4 = digitalio.DigitalInOut(board.D5)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D13)
lcd_d7 = digitalio.DigitalInOut(board.D26)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, LCD_COLUMNS, LCD_ROWS)

# wipe LCD screen before we start
lcd.clear()

##
## Configure our loop variable
##
repeat = True
scroller = LCDLineScroller(write_line, cols=16, row=0, fps=6)

try:
    lcd.clear()
    scroller.start("This is a long message that will scroll forever...")

    # main thread can do other work
    for n in range(20):
        time.sleep(1)

    scroller.set_message("Message updated while running!")

    while True:
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
finally:
    cleanup_display(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7)
