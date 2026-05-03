import pytest
from traffic_light.traffic_light_machine import TrafficLightMachine


def test_initial_state_is_red(capsys):
    sm = TrafficLightMachine()

    # StateChart activates the initial state on construction
    assert sm.red.is_active
    assert not sm.yellow.is_active
    assert not sm.green.is_active

    # on_enter_green() should have printed during initialization
    captured = capsys.readouterr()
    assert "Red state entered." in captured.out

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

def test_cycle_red_green_yellow(capsys):
    sm = TrafficLightMachine()
    capsys.readouterr()  # clear startup output

    sm.cycle()  # red -> green
    sm.cycle()  # green -> yellow
    sm.cycle()  # yellow -> red
    assert sm.red.is_active
    assert not sm.green.is_active
    assert not sm.yellow.is_active

