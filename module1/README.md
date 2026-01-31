# Overview

This week is all about getting set up for the rest of the course.

# Qwiic Shim Setup

The [SparkFun Qwiic Shim](https://www.adafruit.com/product/4463?srsltid=AfmBOop4uiiC7y1YL899XXgjB8vgjPS22l7xIyDs6VNgux3Ahi4JlUGa) is
placed on the Raspberry Pi's GPIO.

Place the Qwiic Shim on the Raspberry Pi's GPIO pins _and then_ connect the 40-pin GPIO ribbon cable.

Once that is done, connect the four-pin cable.

<figure>
  <img src="../images/module1/shim/2_shim_view_1.jpg" alt="Qwiic Shim connected to Raspberry Pi - Angle 1" width="400" />
  <figcaption><em>Figure 1: Qwiic Shim and 4-pin connector</em></figcaption>
</figure>

<figure>
  <img src="../images/module1/shim/3_shim_view_2.jpg" alt="Qwiic Shim connected to Raspberry Pi - Angle 1" width="400" />
  <figcaption><em>Figure 2: Qwiic Shim and 4-pin connector, close up</em></figcaption>
</figure>

<figure>
  <img src="../images/module1/shim/1_shim_overview.jpg" alt="Qwiic Shim connected to Raspberry Pi" width="400" />
  <figcaption><em>Figure 3: Qwiic Shim connected to Raspberry Pi</em></figcaption>
</figure>

# LED Wiring

You will need the 220-ohm resistor, LED, and two jumper wires (one black and one white, 
if you want to follow along with the colors) for this section.

<figure>
  <img src="../images/common/220_ohm_resistor.jpg" alt="220 ohm resistor" width="400" />
  <figcaption><em>Figure 4: 220 ohm resistor</em></figcaption>
</figure>

The white wire for the LED should be placed in __row 7__ of the breadboard, which is connected to GPIO18 on the Raspberry Pi.

<figure>
  <img src="../images/module1/led/1_wire_into_gpio18.jpg" alt="White wire into row 7" width="400" />
  <figcaption><em>Figure 5: White wire into row 7</em></figcaption>
</figure>

The black wire for the LED should be placed in __row 4__ of the breadboard, which is connected to the __ground (GND)__ pin on the Raspberry Pi.

<figure>
  <img src="../images/module1/led/2_wire_into_gnd.jpg" alt="Black wire into row 4" width="400" />
  <figcaption><em>Figure 6: Black wire into row 4</em></figcaption>
</figure>

The LED should be placed so that the longer leg (anode) is in __row 36__ and the shorter leg (cathode) is in __row 35__.

The rest of the wiring should be done as follows:

* The white wire should connect to the anode in __row 36__ from __row 7__ (which we already connected).
* The 220-ohm resistor should connect from __row 35__ to __row 30__ 
* The black wire should connect go from __row 30__ to __ground__ in __row 4__ (which we already connected).

<figure>
  <img src="../images/module1/led/3_led_wiring_angle1.jpg" alt="LED wiring" width="400" />
  <figcaption><em>Figure 7: LED wiring</em></figcaption>
</figure>

<figure>
  <img src="../images/module1/led/4_led_wiring_angle2.jpg" alt="Another angle of LED wiring" width="400" />
  <figcaption><em>Figure 8: Another angle of the LED wiring</em></figcaption>
</figure>