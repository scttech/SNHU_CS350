import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt

MQTT_HOST  = "localhost"
MQTT_PORT  = 1883
MQTT_TOPIC = "traffic_light/state"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(MQTT_HOST, MQTT_PORT)
client.loop_start()

for state in ["red", "green", "yellow"]:
    payload = json.dumps({"timestamp": datetime.now().isoformat(), "state": state})
    client.publish(MQTT_TOPIC, payload)
    print(f"Published: {payload}")
    time.sleep(1)

client.loop_stop()
client.disconnect()
