import paho.mqtt.publish as publish

BROKER = "broker.emqx.io"
TOPIC = "smarthome/actuator/button"

publish.single(TOPIC, '{"command": "toggle"}', hostname=BROKER)
print(f"📤 Sent: 'toggle' to {TOPIC}")
