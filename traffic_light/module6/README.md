# Module 6: Expanding the state machine

We now have three LEDs in our project and we have tested them individually using a few different methods.

Now, it is time to update our traffic light state machine to blink the LEDs.

For the moment we are still looking to keep things simple ([KISS](https://www.geeksforgeeks.org/software-engineering/kiss-principle-in-software-development/) principle).

# Updating the traffic light code

Now, that we have our circuit, we can take a look at updating the code.

## Adding the red LED

We now have all the LEDs and the states defined.  

Note that we have set the initial state to red.  This is because we figured if the system was starting, we would want the
lights to initially be red and then start cycling.  As opposed to telling cars they can start going.

Think about a simple intersection, while we've only modeled one side of the light... we wouldn't necessarily want all the
lights to start in green and then determine how to cycle.  Safer to have all cars stopped as the system comes online.

```python
class TrafficLightMachine(StateChart):
    "A traffic light machine"
    green = State()
    yellow = State()
    red = State(initial=True)
    GREEN_LED_PIN = 18
    RED_LED_PIN = 23
    YELLOW_LED_PIN = 24
    GREEN_LED = LED(GREEN_LED_PIN)
    RED_LED = LED(RED_LED_PIN)
    YELLOW_LED =LED(YELLOW_LED_PIN)
```

## Updating the cycle

Below we update the cycle to transition appropriately.

* Red to Green
* Green to Yellow
* Yellow to Red



```python
    cycle = (
        red.to(green)
        | green.to(yellow)
        | yellow.to(red)
    )
```

## Blinking the LED

We can use the `gpiozero` library to blink the light.

Update both the yellow and green states to blink the appropriate light as well.

```python
    def on_enter_red(self):
        print("Red state entered.")
        self.RED_LED.blink(1.0, 1.0, 1, False)

    def on_exit_red(self):
        print("Red state exited!")
        self.RED_LED.off()
```

# Updating our tests

If we run our tests `sudo ./.venv/bin/python3 -m pytest`

We will see:

```text
FAILED tests/test_traffic_light_machine.py::test_initial_state_is_green - AssertionError: assert False
FAILED tests/test_traffic_light_machine.py::test_cycle_green_to_yellow - AssertionError: assert False
FAILED tests/test_traffic_light_machine.py::test_cycle_yellow_to_green - AssertionError: assert 'Green state exited!' in 'Running cycle from red to green\nRed state exited!\nGreen state entered.\n'
FAILED tests/test_traffic_light_machine_simple.py::test_traffic_light_cycles_between_green_and_yellow - AssertionError: assert False
```

## Fixing the test_initial_state_is_green

We see the first failure was with `FAILED tests/test_traffic_light_machine.py::test_initial_state_is_green - AssertionError: assert False`

As we mentioned earlier, we set the initial state to be red. So, we make the following changes

* Initial state should be red
* Yellow and Green should not be active
* Output should have "Red state entered."

The updated test below is now successful

```python
def test_initial_state_is_red(capsys):
    sm = TrafficLightMachine()

    # StateChart activates the initial state on construction
    assert sm.red.is_active
    assert not sm.yellow.is_active
    assert not sm.green.is_active

    # on_enter_green() should have printed during initialization
    captured = capsys.readouterr()
    assert "Red state entered." in captured.out
```

## Fixing the test_cycle_green_to_yellow 

We now name the test `test_cycle_red_to_green`

* Ensure we get the correct output for the first cycle
* Update the asserts 
* Ensure we get the correct output for the second cycle

```python
def test_cycle_red_to_green(capsys):
    sm = TrafficLightMachine()
    capsys.readouterr()  # clear startup output

    sm.cycle()  # red -> green
    captured = capsys.readouterr()
    assert "Red state exited!" in captured.out
    assert "Green state entered." in captured.out

    sm.cycle()  # green -> yellow

    assert sm.yellow.is_active
    assert not sm.green.is_active
    assert not sm.red.is_active

    captured = capsys.readouterr()
    assert "Green state exited!" in captured.out
    assert "Yellow state entered." in captured.out
```

## Fix the test_cycle_yellow_to_green test

Update the test to `test_cycle_red_green_yellow`

Now, we just want to test that when we make a complete cycle we are back in the red state and both the green and yellow
states are not active

```python
def test_cycle_red_green_yellow(capsys):
    sm = TrafficLightMachine()
    capsys.readouterr()  # clear startup output

    sm.cycle()  # red -> green
    sm.cycle()  # green -> yellow
    sm.cycle()  # yellow -> red
    assert sm.red.is_active
    assert not sm.green.is_active
    assert not sm.yellow.is_active
```

## Fix the test_traffic_light_cycles_between_green_and_yellow

The last failure is in `test_traffic_light_cycles_between_green_and_yellow` from `test_traffic_light_machine_simple.py`
here we are testing the active state for each cycle.

* Verify we start in red
* Move to green
* Move to yellow

```python
def test_traffic_light_cycles_between_red_green_yellow():
    sm = TrafficLightMachine()

    assert sm.red.is_active

    sm.cycle()
    assert sm.green.is_active

    sm.cycle()
    assert sm.yellow.is_active
```

# Running our traffic light

We update the `traffic_light.py` to continually run through the cycles and to catch a keyboard interrupt so that
we can shutdown nicely.

```python
def main() -> None:
    sm = TrafficLightMachine()
    try:
        while True:
            sm.send("cycle")
            sm.send("cycle")
            sm.send("cycle")
    except KeyboardInterrupt:
        pass
    finally:
        print("\nExiting...")

if __name__ == "__main__":
    main()
```

We can run everything with 

`sudo ./.venv/bin/python3 traffic_light.py`

# Enhancing the traffic light 

After running the project you may notice some issues.  Let us take a look at them.

## Lights are off between transitions

If you run this code you should now see the lights cycling between red → green → yellow

There is one major issue we should notice about how the traffic light is operating.

The traffic light is off between transitions, so when exiting the red state the light goes off but no lights are on.
Which is not how a traffic light operates.  

This is a bug that we introduced when initially coding the project with 

```python
self.RED_LED.blink(1.0, 1.0, 1, False)
```

This could be more clearly written as

```python
self.RED_LED.blink(on_time=1.0, off_time=1.0, n=1, background=False)
```

We are setting the `off_time` which is causing the light to be off for an extended period of time.  We can update the
code to set the `off_time` to zero and rerun the code.  Which gives us a better approximation to a traffic light's actual
behavior.

```python
self.RED_LED.blink(on_time=1.0, off_time=0.0, n=1, background=False)
```

## Lights are too quick

We have the lights set to be on for one second.  That isn't a lot of time to let traffic flow through our light.

We can take a look at the Manual on Uniform Traffic Control Devices ([MUTCD](https://mutcd.fhwa.dot.gov/)) and 
the [Traffic Signal Timing Manual](https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm)
to help determine how long each light might be on for.

There is a lot of information in there, we will be going with the general setup of:

* Green - 45 seconds
* Yellow - 6 seconds
* Red - 39 seconds

# Conclusion

There is a lot of thought that goes into the placement and setup of traffic lights.  We have only just touched the 
surface, but that is all we needed for our purposes.

In the next [module](../module7/README.md) we will take a brief look at state machine diagrams.