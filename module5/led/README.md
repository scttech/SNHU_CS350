# Wiring the LED

We will need to move the red LED and then place a blue LED. It is recommended that you 
complete the wiring for the LEDs before moving on to the button so that you are able to test the LEDs 
before the button.

# Moving the Red LED

Move the red LED to __Row 63__, __Column G__ and __Row 64__, __Column G__ as shown in Figure 1.

<figure>
    <img src="../../images/module5/led_setup/1_red_led_moved.jpg" alt="Moving the red LED" width="400" />
    <figcaption>Figure 1: Moving the Red LED</figcaption>
</figure>

Move the 220 Ohm resistor to __Row 63__, __Column I__ and __Row 59__, __Column I__ as shown in Figure 2.

<figure>
    <img src="../../images/module5/led_setup/2_resistor_added.jpg" alt="Moving the red LED resistor" width="400" />
    <figcaption>Figure 2: Moving the 220-ohm resistor for the Red LED</figcaption>
</figure>

Move the white wire to __Row__ 64__, __Column F__ and move the black wire to __Row 59__, __Column J__ as shown in Figure 3.

<figure>
    <img src="../../images/module5/led_setup/3_wiring_the_red_led.jpg" alt="Wiring the red LED" width="400" />
    <figcaption>Figure 3: Wiring the Red LED</figcaption>
</figure>

Then validate the Red LED is working by running the test script.  The GPIO pin has not changed, so the script should
work without modification.

<figure>
    <img src="../../images/module5/led_setup/4_red_led_validated.jpg" alt="Validating the Red LED" width="400" />
    <figcaption>Figure 4: Validating the Red LED</figcaption>
</figure>

# Placing the Blue LED

Now it is time for the Blue LED.

<figure>
    <img src="../../images/common/blue_led.jpg" alt="Blue LED" width="400" />
    <figcaption>Figure 5: Blue LED</figcaption>
</figure>

Place the blue LED in __Row 54__, __Column G__ and __Row 55__, __Column G__ and __Row 54__, __Column G__ as shown in Figure 6.

<figure>
    <img src="../../images/module5/led_setup/6_blue_led_placement.jpg" alt="Placing the blue LED" width="400" />
    <figcaption>Figure 6: Placing the Blue LED</figcaption>
</figure>

Next, take a 220-Ohm resistor as shown in Figure 7.

<figure>
    <img src="../../images/common/220_ohm_resistor.jpg" alt="220 Ohm Resistor" width="400" />
    <figcaption>Figure 7: 220 Ohm Resistor</figcaption>
</figure>

Place the 220-Ohm resistor in __Row 49__, __Column I__ and __Row 53__, __Column I__ as shown in Figure 8.

<figure>
    <img src="../../images/module5/led_setup/8_220_ohm_resistor_placement.jpg" alt="Placing the resistor for the blue LED" width="400" />
    <figcaption>Figure 8: Placing the resistor for the Blue LED</figcaption>
</figure>

Place a yellow wire (note the breadboard was rotated) from __Row 54__, __Column F__ as shown in Figure 9.

<figure>
    <img src="../../images/module5/led_setup/9_wire_from_pin23.jpg" alt="Placing the signal wire for the blue LED" width="400" />
    <figcaption>Figure 9: Placing the signal wire for the Blue LED</figcaption>
</figure>

To __GPIO 23__ on __Row 9__ as shown in Figure 10.

<figure>
    <img src="../../images/module5/led_setup/10_pin23_wire.jpg" alt="Connecting the signal wire for the blue LED to GPIO 23" width="400" />
    <figcaption>Figure 10: Connecting the signal wire for the Blue LED to GPIO 23</figcaption>
</figure>

Next, we take a green wire from GND on __Row 9__ as shown in Figure 11.

<figure>
    <img src="../../images/module5/led_setup/11_gnd_wire.jpg" alt="Placing the ground wire for the blue LED" width="400" />
    <figcaption>Figure 11: Placing the ground wire for the Blue LED</figcaption>
</figure>

Finally, connect the green wire to __Row 49__, __Column J__ as shown in Figure 12.

<figure>
    <img src="../../images/module5/led_setup/12_gnd_wire_connection.jpg" alt="Connecting the ground wire for the blue LED" width="400" />
    <figcaption>Figure 12: Connecting the ground wire for the Blue LED</figcaption>
</figure>

# Validation

Now we can validate the Blue LED is working by running the test script.

<figure>
    <img src="../../images/module5/led_setup/13_blue_led_validation.jpg" alt="Validating the blue LED" width="400" />
    <figcaption>Figure 13: Validating the Blue LED</figcaption>
</figure>

We can also validate the Red LED is still working by running the test script again.

<figure>
    <img src="../../images/module5/led_setup/14_both_leds_for_fun.jpg" alt="Validating the red LED again" width="400" />
    <figcaption>Figure 14: Validating the Red LED again</figcaption>
</figure>

# Wiring Overview

Here is an overview of the wiring for the LEDs.

<figure>
    <img src="../../images/module5/led_setup/15_led_wiring_overview.jpg" alt="LED wiring overview" width="400" />
    <figcaption>Figure 15: LED wiring overview</figcaption>
</figure>

Here is an overview of the wiring for the GPIO pins

<figure>
    <img src="../../images/module5/led_setup/16_gpio_wiring_overview.jpg" alt="GPIO wiring overview" width="400" />
    <figcaption>Figure 16: GPIO wiring overview</figcaption>
</figure>


