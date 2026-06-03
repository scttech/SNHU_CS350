import json
import pytest
from traffic_light.traffic_light_machine import TrafficLightMachine, MQTT_TOPIC


def test_initial_state_is_red(capsys, mock_mqtt_client):
    sm = TrafficLightMachine(mqtt_client=mock_mqtt_client)

    assert sm.red.is_active
    assert not sm.yellow.is_active
    assert not sm.green.is_active

    captured = capsys.readouterr()
    assert "Red state entered." in captured.out
    mock_mqtt_client.publish.assert_called_once_with(MQTT_TOPIC, json.dumps({"state": "red"}))


def test_cycle_red_to_green(capsys, mock_mqtt_client):
    sm = TrafficLightMachine(mqtt_client=mock_mqtt_client)
    capsys.readouterr()
    mock_mqtt_client.reset_mock()

    sm.cycle()  # red -> green
    captured = capsys.readouterr()
    assert "Red state exited!" in captured.out
    assert "Green state entered." in captured.out
    mock_mqtt_client.publish.assert_called_once_with(MQTT_TOPIC, json.dumps({"state": "green"}))

    mock_mqtt_client.reset_mock()
    sm.cycle()  # green -> yellow

    assert sm.yellow.is_active
    assert not sm.green.is_active
    assert not sm.red.is_active

    captured = capsys.readouterr()
    assert "Green state exited!" in captured.out
    assert "Yellow state entered." in captured.out
    mock_mqtt_client.publish.assert_called_once_with(MQTT_TOPIC, json.dumps({"state": "yellow"}))


def test_cycle_red_green_yellow(capsys, mock_mqtt_client):
    sm = TrafficLightMachine(mqtt_client=mock_mqtt_client)
    capsys.readouterr()
    mock_mqtt_client.reset_mock()

    sm.cycle()  # red -> green
    sm.cycle()  # green -> yellow
    sm.cycle()  # yellow -> red

    assert sm.red.is_active
    assert not sm.green.is_active
    assert not sm.yellow.is_active

    assert mock_mqtt_client.publish.call_count == 3