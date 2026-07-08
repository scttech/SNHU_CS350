# Overview

This will help you with the LED wiring

# LED Wiring

You will need the following:

* 220-ohm resistor
* LED
* Two jumper wires (one black and one white, if you want to follow along with the colors) for this section.

<figure>
  <img src="../../images/common/220_ohm_resistor.jpg" alt="220 ohm resistor" width="400" />
  <figcaption><em>Figure 4: 220 ohm resistor</em></figcaption>
</figure>

The white wire for the LED should be placed in __Row 7__, __Column H__ of the breadboard, which is connected to __GPIO 18__ on the Raspberry Pi.

<figure>
  <img src="../../images/module1/led/1_wire_into_gpio18.jpg" alt="White wire into row 7" width="400" />
  <figcaption><em>Figure 5: White wire into row 7</em></figcaption>
</figure>

The black wire for the LED should be placed in __Row 4__, __Column H__ of the breadboard, which is connected to the __ground (GND)__ pin on the Raspberry Pi.

<figure>
  <img src="../../images/module1/led/2_wire_into_gnd.jpg" alt="Black wire into row 4" width="400" />
  <figcaption><em>Figure 6: Black wire into row 4</em></figcaption>
</figure>

The LED should be placed so that the longer leg (anode) is in __Row 36__, __Column I__ and the shorter leg (cathode) is in __Row 35__, __Column I__.

The rest of the wiring should be done as follows:

* The white wire should connect to the longer leg (anode) in __Row 36__, __Column H__ from __Row 7__, __Column H__ (which we already connected).
* The 220-ohm resistor should connect from __Row 35__, __Column G__ to __Row 30__, __Column G__ 
* The black wire should connect go from __Row 30__, __Column F__ to __ground__ in __Row 4__, __Column H__ (which we already connected).

<figure>
  <img src="../../images/module1/led/3_led_wiring_angle1.jpg" alt="LED wiring" width="400" />
  <figcaption><em>Figure 7: LED wiring</em></figcaption>
</figure>

<figure>
  <img src="../../images/module1/led/4_led_wiring_angle2.jpg" alt="Another angle of LED wiring" width="400" />
  <figcaption><em>Figure 8: Another angle of the LED wiring</em></figcaption>
</figure>