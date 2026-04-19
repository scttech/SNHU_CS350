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
