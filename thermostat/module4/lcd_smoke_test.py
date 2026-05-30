# lcd_smoke_test.py - Minimal code to display a message to Raspberry Pi 4
# Run with: sudo python3 lcd_smoke_test.py

import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

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
lcd.message = "Hello Pi!"

print("Message sent. Check LCD.")
input("Press Enter to exit and clean up...")

lcd.clear()
for pin in [lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7]:
    pin.deinit()