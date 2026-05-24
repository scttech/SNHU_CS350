from traffic_light.traffic_light_machine import TrafficLightMachine


def test_traffic_light_cycles_between_red_green_yellow():
    sm = TrafficLightMachine()

    assert sm.red.is_active

    sm.cycle()
    assert sm.green.is_active

    sm.cycle()
    assert sm.yellow.is_active