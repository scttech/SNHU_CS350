import json
import time
import os
import psycopg2
import paho.mqtt.client as mqtt

MQTT_HOST  = os.getenv("MQTT_HOST", "mosquitto")
MQTT_PORT  = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = "traffic_light/state"

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "traffic_light")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")


def connect_db():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT,
                dbname=DB_NAME, user=DB_USER, password=DB_PASS
            )
            conn.autocommit = True
            print("Connected to PostgreSQL")
            return conn
        except psycopg2.OperationalError as e:
            print(f"DB not ready, retrying in 2s: {e}")
            time.sleep(2)


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to MQTT broker (rc={reason_code})")
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    conn = userdata["conn"]
    try:
        payload = json.loads(msg.payload.decode())
        state = payload["state"]
        created_on = payload.get("timestamp")
        with conn.cursor() as cur:
            if created_on:
                cur.execute(
                    "INSERT INTO traffic_state_history (created_on, state) VALUES (%s, %s)",
                    (created_on, state)
                )
            else:
                cur.execute(
                    "INSERT INTO traffic_state_history (state) VALUES (%s)",
                    (state,)
                )
        print(f"Logged state: {state} at {created_on}")
    except Exception as e:
        print(f"Error storing message: {e}")


def main():
    conn = connect_db()

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.user_data_set({"conn": conn})
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_forever()


if __name__ == "__main__":
    main()