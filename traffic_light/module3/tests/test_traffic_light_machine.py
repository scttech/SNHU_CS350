import pytest
from traffic_light.traffic_light_machine import TrafficLightMachine


def test_initial_state_is_green(capsys):
    sm = TrafficLightMachine()

    # StateChart activates the initial state on construction
    assert sm.green.is_active
    assert not sm.yellow.is_active

    # on_enter_green() should have printed during initialization
    captured = capsys.readouterr()
    assert "Green state entered." in captured.out


def test_cycle_green_to_yellow(capsys):
    sm = TrafficLightMachine()
    capsys.readouterr()  # clear startup output

    sm.cycle()

    assert sm.yellow.is_active
    assert not sm.green.is_active

    captured = capsys.readouterr()
    assert "Green state exited!" in captured.out
    assert "Yellow state entered." in captured.out


def test_cycle_yellow_to_green(capsys):
    sm = TrafficLightMachine()
    capsys.readouterr()  # clear startup output

    sm.cycle()  # green -> yellow
    captured = capsys.readouterr()
    assert "Green state exited!" in captured.out
    assert "Yellow state entered." in captured.out

    sm.cycle()  # yellow -> green

    assert sm.green.is_active
    assert not sm.yellow.is_active

    captured = capsys.readouterr()
    assert "Yellow state exited!" in captured.out
    assert "Green state entered." in captured.out