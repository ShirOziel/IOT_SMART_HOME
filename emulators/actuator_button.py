import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "smarthome/actuator/button"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("🟢 Button Emulator Started - Press Enter to toggle...")

try:
    while True:
        input("🔘 Press Enter to send TOGGLE command...")
        client.publish(TOPIC, '{"command": "toggle"}')
        print(f"📤 Sent: {{'command': 'toggle'}} to {TOPIC}")

except KeyboardInterrupt:
    print("\n❌ Stopping Button Emulator...")
    client.disconnect()
