# lcd_date_time.py - Run a display with the date/time
# Run with: sudo python3 lcd_date_time.py

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
from datetime import datetime
import time

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D17)
lcd_en = digitalio.DigitalInOut(board.D27)
lcd_d4 = digitalio.DigitalInOut(board.D5)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D13)
lcd_d7 = digitalio.DigitalInOut(board.D26)

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

lcd.clear()

repeat = True
while repeat:
    try:
        now = datetime.now()
        lcd.message = now.strftime('%b %d  %H:%M:%S\nus: %f')

        ## Sleep until the next whole second to prevent clock drift
        time.sleep(1 - (time.time() % 1))

        ## To see the clock drift use time.sleep(1) instead of the above sleep, when the microseconds (us) nears
        ## 999999 microseconds you will see the second display skip
        # time.sleep(1)
    except KeyboardInterrupt:
        repeat = False

lcd.clear()
for pin in [lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7]:
    pin.deinit()