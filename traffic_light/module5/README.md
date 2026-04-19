# Module 5: Adding the Red LED

This module is similar to the previous module. We will be wiring up the red LED and testing it.

# Wiring the red LED

## Needed components

Again, in addition to a couple of wires, we will need a red LED

<figure>
  <img src="../images/common/red_led.jpg" alt="Red LED" width="400" />
  <figcaption><em>Figure 1: Red LED</em></figcaption>
</figure>

And a 220-ohm resistor

<figure>
  <img src="../images/common/220ohm_resistor.jpg" alt="220 resistor" width="400" />
  <figcaption><em>Figure 2: 220-ohm resistor</em></figcaption>
</figure>

## Wiring

Again, the colors of the wire do not matter, we only mention them as a matter of
additional reference.

We are using an orange wire to Pin 23 in __Row 8, Column H__

<figure>
  <img src="../images/module5/1_orange_to_pin23.jpg" alt="Orange wire to pin 23" width="400" />
  <figcaption><em>Figure 3: Orange wire to GPIO Pin 23</em></figcaption>
</figure>

Connect the orange wire to __Row 43, Column J__

<figure>
  <img src="../images/module5/2_orange_to_row43.jpg" alt="orange wire placement" width="400" />
  <figcaption><em>Figure 4: Orange wire to row 43</em></figcaption>
</figure>

We place the resistor in __Row 43, Column H__ and over to __Row 47, Column H__

<figure>
  <img src="../images/module5/3_resistor_row43_to_row47.jpg" alt="resistor placement" width="400" />
  <figcaption><em>Figure 5: Resistor placement</em></figcaption>
</figure>

The red LED goes from __Row 47, Column F__ to __Row 48, Column F__

<figure>
  <img src="../images/module5/4_red_led_row47_and_row48.jpg" alt="red led placement" width="400" />
  <figcaption><em>Figure 6: Red LED placement</em></figcaption>
</figure>

Connect the gray wire __Row 48, Column J__

<figure>
  <img src="../images/module5/5_grey_wire_to_row48.jpg" alt="gray wire placement" width="400" />
  <figcaption><em>Figure 7: Place the gray wire</em></figcaption>
</figure>

Ground the gray wire in __Row 15, Column J__

<figure>
  <img src="../images/module5/6_grey_wire_to_row15_angle1.jpg" alt="gray wire, angle 1" width="400" />
  <figcaption><em>Figure 8: Grounding the gray wire, angle 1</em></figcaption>
</figure>

Another angle of the gray wire connected to GND

<figure>
  <img src="../images/module5/7_grey_wire_to_row15_angle2.jpg" alt="gray wire, angle 2" width="400" />
  <figcaption><em>Figure 9: Gray wire, angle 2</em></figcaption>
</figure>

# Testing the red LED

As we saw in the previous module, we have a few options for testing the LED.

## Run the led_tester.py code

First we can run the `led_tester.py` program from module 1 

`sudo python3 led_tester.py RED`

We should see the following output

`RED LED ON (pin 23). Press Ctrl+C to exit.`

And probably more importantly, we will see the red LED lighting up.

## Use the gpio command

We can also use the `gpio` command

First set pin 23 to be output with

`sudo gpio -g mode 23 out`

Then toggle pin 23 

`sudo gpio -g toggle 23`

Then we can read the pins with

`sudo gpio readall`

And see the following output

```
 +-----+-----+---------+------+---+---Pi 3B--+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
                                       || 16 | 1 | OUT  | GPIO. 4 | 4   | 23  |
```

## Use the gpio-pininfo.sh

We also have the `gpio-pininfo.sh` which wraps the `gpio` command

We run

`sudo ./gpio-pininfo.sh 23`

And receive the output

```
GPIO Diagnostic
---------------------------
BCM Pin:       23
wPi Pin:       4
Physical Pin:  16
Name:          GPIO. 4
Mode:          OUT
Value:         HIGH (1)
```

# Wrap up

We should have now confirmed that our LEDs are all working.

In the next module, we will update our state machine so that we can cycle through the states and turn each LED on and off
so that we can begin to mimic a working traffic light.



