# Debugging

Often we wonder why LED is not lighting up or why the button is not working. When it comes to our circuit a multimeter
can be a helpful tool.  However, not everyone has a multimeter on hand, so we will be using a simple method to check 
if our circuit is working by bypassing the Python code.

There is a nice community project called `wiringpi` that allows us to control the GPIO pins directly from the terminal. 
This can be very useful for debugging purposes, as it allows us to test our circuit without having to run our Python code.

## Prerequisites

The original `wiringpi` project is no longer maintained, so we unfortunately cannot simply use `sudo apt-get install wiringpi` to install it.

Instead, we will get the project from GitHub and install it manaully.

```bash
git clone https://github.com/WiringPi/WiringPi.git
cd WiringPi
./build
```

Once that completes, we should now have access to the `gpio` command. Note that you will have to use `sudo` to run the command.

## Testing the LED

Assuming we have setup our LED on GPIO pin 18, we can test it by running the following command

```bash 
sudo gpio -g mode 18 out
sudo gpio -g toggle 18
```

This will set GPIO pin 18 to output mode and toggle its state.  

If the LED is working correctly, it should light up when you run the toggle command. 
You can run the toggle command multiple times to see the LED turn on and off.

There is also a `sudo gpio readall`

Which produces output such as the below on my Raspberry Pi.

```
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 1 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 1 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 1 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 1 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
```

You can look at this [sample code](../pin_18_debug.py) to see how the output from gpio changes while our code is running.

You will set BCM Pin 18 set to mode OUT and V change from 0 to 1.  

Then V will change back to 0.

Finally, after we perform the GPIO clean up you will see the mode change back to IN and V change back to 0.

I have also provided a [shell script](../gpio-pininfo.sh) that provides formatted output for a single pin which can
be useful for debugging purposes and might be a bit easier to read for a single pin.





