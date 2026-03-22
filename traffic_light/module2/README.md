# Module 2: Coding of the traffic light state machine for the green light

# Setup required dependencies

We will now start managing our project using a `requirements.txt` file. 
This file will contain all the dependencies for our project. As we add more functionality in
subsequent modules, we will add more dependencies to this file.

We will need to install the `python-statemachine` library with the following command:

In the previous module we installed the following dependencies:

* `python3-dev` 
* `RPi.GPIO`

To this we will now add `python-statemachine`

So, our `requirements.txt` file will now look like this:

```
python3-dev
RPi.GPIO
python-statemachine
```

When we create a new virtual environment, we can install all the dependencies in one go with the following command:

`python3 -m pip install -r requirements.txt`

# Setup the virtual environment

To keep things clear, we will be creating a new virtual environment for each module. This will help us keep track of the dependencies 
for each module. This way, we can keep track of how our project grows from module ot module.

Create a new virtual enviornment with the following command:

`python3 -m venv .venv`

Remember to activate the virtual environment with the following command:
`source .venv/bin/activate`

Install the dependencies with the following command:

`python3 -m pip install -r requirements.txt`

We can also choose to save the requirements with 

`python3 -m pip freeze > requirements.txt`

This helps us keep track of the exact versions of the dependencies we are using.  Why would we want to do that?
In order to ensure that we have repeatable builds.  If we don't specify the versions of the dependencies, we might end 
up with different versions of the dependencies when we install them in the future. This can lead to compatibility 
issues and bugs that are hard to track down. By specifying the versions of the dependencies, we can ensure that we 
have a consistent environment for our project.

The flip side of this is that we might end up with outdated dependencies that have security vulnerabilities. So, it's 
important to keep track of the dependencies and update them regularly. We can use tools like 
[dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide) to 
help automate this process.

Finally, remember to deactivate (but not just yet) the virtual environment when you are done with the following command:
`deactivate`

To make sure everything is working, we can run the `led_tester.py` script from the previous module with the following
command:

`sudo python3 ../module1/led_tester.py GREEN`

We should see the green LED turn on.

# Coding the state machine for the green light

This code is based off the sample code from the `python-statemachine` library. You should be able to find the complete
sample on their site [here](https://python-statemachine.readthedocs.io/en/latest/). However, in this project we will be
taking it in smaller steps.

Let us take a look at the `traffic_light_machine.py` that is in this module.  Below is the full listing, then we will
break it down.

```python
from statemachine import StateChart, State

class TrafficLightMachine(StateChart):
    "A traffic light machine"
    green = State(initial=True)
    yellow = State()

    cycle = (
        green.to(yellow)
        | yellow.to(green)
    )

    def before_cycle(self, event: str, source: State, target: State):
        print(f"Running {event} from {source.id} to {target.id}")

    def on_enter_green(self):
        print("Green state entered.")

    def on_exit_green(self):
        print("Green state exited!")

    def on_enter_yellow(self):
        print("Yellow state entered.")

    def on_exit_yellow(self):
        print("Yellow state exited!")
```

## Imports

We import `StateChart` and `State` from `statemachine` with the following line:

```python
from statemachine import StateChart, State
```

## Define a class

We define a class named `TrafficLightMachine` with the following line:

```python
class TrafficLightMachine(StateChart):
```

## Defining states

A state is a specific stable condition in our system.  Typically, a state machine can only be in one state at a time.  Think of 
the possible states of "RUNNING" and "STOPPED".  We cannot be in both states at once. 

In our `TrafficLightMachine` we have defined two states that represent whether the light is Green or Yellow.  We defined
these with:

```python
green = State(initial=True)
yellow = State()
```

In the above example, notice that we also defined the green state as the initial state.

## State transitions

We need the ability to move between states.  For instance, if we are "STOPPED" then we would certainly want a way to
get into a "RUNNING" state.  

The way we do this is with a transition.  By defining transitions, we can define the appropriate states that a state
machine can move through. In our traffic light example, we want the "green" state to transition to "yellow".  It would
be bad if the "green" state transitioned directly to "red" without allowing cars to slow down and stop.  

We called our transition `cycle` and defined it as:

```python
cycle = (
    green.to(yellow)
    | yellow.to(green)
)
```

Ignore for a moment that the yellow → green transition does not make sense for a traditional traffic light (we will
address that later).

We define two transitions.

* Green to Yellow
* Yellow to Green

## State Actions

A state action is a side effect that runs during a state change.

We define several actions:

```python
def before_cycle(self, event: str, source: State, target: State):
    print(f"Running {event} from {source.id} to {target.id}")

def on_enter_green(self):
    print("Green state entered.")

def on_exit_green(self):
    print("Green state exited!")

def on_enter_yellow(self):
    print("Yellow state entered.")

def on_exit_yellow(self):
    print("Yellow state exited!")
```

These should be self explanatory. The `on_enter_<state>` are called upon entering a state and `on_exit_<state>` are called
when exiting. We also have a `before_<event>` which happens before the cycle event.

# Running our state machine

This module also has a simple script to make use of our state machine. The `traffic_light.py` script is shown below:

```python
from traffic_light_machine import TrafficLightMachine


def main() -> None:
    sm = TrafficLightMachine()
    sm.send("cycle")
    sm.send("cycle")

if __name__ == "__main__":
    main()
```

Running our script we get the following output.

```
Green state entered.
Running cycle from green to yellow
Green state exited!
Yellow state entered.
Running cycle from yellow to green
Yellow state exited!
Green state entered.
```

In the next [module](../module3/README.md) we'll look at further testing out state machine.