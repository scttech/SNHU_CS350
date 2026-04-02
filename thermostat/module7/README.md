# Overview

This week we will be adding a few more buttons to finish the circuit.

# Adding the buttons

Although you can choose any button colors you want, since this project is evolving into the thermostat it makes sense
to choose a red button (heating/raise temperature) and blue button (cooling/lower temperature)

<figure>
  <img src="../images/module7/1_button_components.jpg" alt="" width="400" />
  <figcaption><em>Figure 1: Button components</em></figcaption>
</figure>

Placing the red button on __Row 31__ and __Row 33__

<figure>
  <img src="../images/module7/2_placing_red_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 2: Red button position</em></figcaption>
</figure>

Placing the blue button on __Row 37__ and __Row 39__

<figure>
  <img src="../images/module7/3_placing_blue_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 3: Blue button position</em></figcaption>
</figure>

# Button wiring

Placing the 10k resistor for the red button on __Row 31__ over to the __3.3+__ volt column

<figure>
  <img src="../images/module7/4_10k_resistor.jpg" alt="" width="400" />
  <figcaption><em>Figure 4: 10k-ohm resistor for red button</em></figcaption>
</figure>

Placing the 10k resistor for the blue button on __Row 37__ over to the __3.3+__ volt column

<figure>
  <img src="../images/module7/5_10k_resistor.jpg" alt="" width="400" />
  <figcaption><em>Figure 5: 10k-ohm resistor for blue button</em></figcaption>
</figure>

For the red button, placing a green wire for the GND on __Row 33, Column I__

<figure>
  <img src="../images/module7/6_wiring_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 6: Wiring red button</em></figcaption>
</figure>

Grounding the green wire to the breakout board in __Row 11, Column I__

<figure>
  <img src="../images/module7/7_wiring_red_button_to_gnd.jpg" alt="" width="400" />
  <figcaption><em>Figure 7: Green wire to GND</em></figcaption>
</figure>

For the blue button, placing a blue wire for the GND on __Row 39, Column I__

<figure>
  <img src="../images/module7/8_wiring_blue_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 8: Wiring blue button</em></figcaption>
</figure>

Grounding the blue wire to the breakout board in __Row 11, Column I__

<figure>
  <img src="../images/module7/9_wiring_blue_button_to_gnd.jpg" alt="" width="400" />
  <figcaption><em>Figure 9: Blue wire to GND</em></figcaption>
</figure>

For the red button adding a purple wire for the GPIO pin, opposite the resistor on __Row 31, Column I__

<figure>
  <img src="../images/module7/10_wiring_red_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 10: Purple wire placement</em></figcaption>
</figure>

Placing the purple wire at __GPIO Pin 25__ in __Row 12, Column H__

<figure>
  <img src="../images/module7/11_wiring_red_button_to_gpio.jpg" alt="" width="400" />
  <figcaption><em>Figure 11: Purple wire to GPIO 25, angle 1</em></figcaption>
</figure>

Another angle of the purple wire for __GPIO Pin 25__

<figure>
  <img src="../images/module7/12_wiring_red_button_to_gpio_angle2.jpg" alt="" width="400" />
  <figcaption><em>Figure 12: Purple wire to GPIO 25, angle 2</em></figcaption>
</figure>

For the blue button, add a gray wire at __Row 37, Column I__

<figure>
  <img src="../images/module7/13_wiring_blue_button.jpg" alt="" width="400" />
  <figcaption><em>Figure 13: Gray wire for blue button</em></figcaption>
</figure>

The gray wire goes to __GPIO Pin 12__ in __Row 17, Column H__

<figure>
  <img src="../images/module7/14_wiring_blue_button_to_gpio.jpg" alt="" width="400" />
  <figcaption><em>Figure 14: Gray wire to GPIO 12</em></figcaption>
</figure>

# Testing LEDs

Verifying both LEDs turn on

<figure>
  <img src="../images/module7/15_both_lights_on.jpg" alt="" width="400" />
  <figcaption><em>Figure 15: Testing both lights on</em></figcaption>
</figure>

Verifying the red LED turns on

<figure>
  <img src="../images/module7/16_red_light_only.jpg" alt="" width="400" />
  <figcaption><em>Figure 16: Testing red light on</em></figcaption>
</figure>

Verifying the blue LED turns on

<figure>
  <img src="../images/module7/17_blue_light_only.jpg" alt="" width="400" />
  <figcaption><em>Figure 17: Testing blue light on</em></figcaption>
</figure>
