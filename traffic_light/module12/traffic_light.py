import argparse
from traffic_light.traffic_light_machine import TrafficLightMachine
from statemachine.contrib.diagram import DotGraphMachine


def generate_diagram(output_path: str) -> None:
    try:
        graph = DotGraphMachine(TrafficLightMachine)
        dot = graph()
        dot.set_label("Traffic Light State Machine")
        dot.set_labelloc("t")
        dot.write_png(output_path + "/traffic_light_diagram.png")
        print(f"State diagram saved to {output_path}/traffic_light_diagram.png")
    except ImportError:
        print("Error: 'graphviz' package is required. Install it with: pip install graphviz")
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description="Traffic Light State Machine")
    parser.add_argument(
        "--diagram",
        nargs="?",
        const=".",
        metavar="OUTPUT_PATH",
        help="Generate a state diagram PNG (default output is : CURRENT_DIRECTORY/traffic_light_diagram.png)",
    )
    parser.add_argument(
        "--mqtt-host",
        default="localhost",
        metavar="HOST",
        help="Hostname or IP of the MQTT broker (default: localhost)",
    )
    args = parser.parse_args()

    if args.diagram is not None:
        generate_diagram(args.diagram)
        return

    sm = TrafficLightMachine(mqtt_host=args.mqtt_host)
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