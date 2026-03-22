from traffic_light_machine import TrafficLightMachine


def main() -> None:
    sm = TrafficLightMachine()
    sm.send("cycle")
    sm.send("cycle")

if __name__ == "__main__":
    main()
