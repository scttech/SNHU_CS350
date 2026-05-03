from traffic_light.traffic_light_machine import TrafficLightMachine


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
