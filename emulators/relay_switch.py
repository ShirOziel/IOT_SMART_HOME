import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
CONTROL_TOPIC = "smarthome/control/relay"
STATUS_TOPIC = "smarthome/relay"

relay_state = False  # False = OFF, True = ON

def on_connect(client, userdata, flags, rc):
    """Subscribe to the control topic when connected."""
    if rc == 0:
        print(f"✅ Connected to MQTT Broker - Subscribed to {CONTROL_TOPIC}")
        client.subscribe(CONTROL_TOPIC)
    else:
        print("❌ Connection failed")

def on_message(client, userdata, msg):
    """Handle MQTT messages for relay control."""
    global relay_state
    command = msg.payload.decode("utf-8").strip().lower()
    
    if command == "on":
        relay_state = True
        print("✅ Relay TURNED ON")
    elif command == "off":
        relay_state = False
        print("❌ Relay TURNED OFF")
    
    # פרסום סטטוס עדכני של הממסר
    client.publish(STATUS_TOPIC, "ON" if relay_state else "OFF")
    print(f"📤 Relay Status Sent: {'ON' if relay_state else 'OFF'} to {STATUS_TOPIC}")

# יצירת חיבור ל-MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

print("📡 Relay Emulator Started - Listening for ON/OFF commands...")

# הרצת לולאת MQTT לניהול התקשורת
client.loop_forever()
