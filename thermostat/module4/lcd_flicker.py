from time import sleep

##
## These are the packages that we need to pull in so that we can work
## with the GPIO interface on the Raspberry Pi board and work with
## the 16x2 LCD display
##
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd


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
while repeat:
    try:

        # This loop goes as fast as possible, the clear will help cause visual flickering
        lcd.clear()
        lcd_line_1 = 'Display\n'
        lcd_line_2 = 'Flicker...'

        # combine both lines into one update to the display
        lcd.message = lcd_line_1 + lcd_line_2

    except KeyboardInterrupt:
        ##
        ## When the user enters CTRL-C at the console, cleanup the
        ## GPIO pins and exit.
        ##
        cleanup_display(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7)
        repeat = False