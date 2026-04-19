from traffic_light.traffic_light_machine import TrafficLightMachine


def test_traffic_light_cycles_between_green_and_yellow():
    sm = TrafficLightMachine()

    assert sm.green.is_active

    sm.cycle()
    assert sm.yellow.is_active

    sm.cycle()
    assert sm.green.is_active