from statemachine import StateChart, State
from gpiozero import LED


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

    cycle = (
        red.to(green)
        | green.to(yellow)
        | yellow.to(red)
    )

    def __init__(self):
        super().__init__()

    def before_cycle(self, event: str, source: State, target: State):
        print(f"Running {event} from {source.id} to {target.id}")

    def on_enter_red(self):
        print("Red state entered.")
        self.RED_LED.blink(39.0, 0.0, 1, False)

    def on_exit_red(self):
        print("Red state exited!")
        self.RED_LED.off()

    def on_enter_green(self):
        print("Green state entered.")
        self.GREEN_LED.blink(45.0, 0.0, 1, False)

    def on_exit_green(self):
        print("Green state exited!")
        self.GREEN_LED.off()

    def on_enter_yellow(self):
        print("Yellow state entered.")
        self.YELLOW_LED.blink(6.0, 0.0, 1, False)

    def on_exit_yellow(self):
        print("Yellow state exited!")
        self.YELLOW_LED.off()
