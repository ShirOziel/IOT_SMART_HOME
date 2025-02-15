import sqlite3

# Database file
DB_NAME = "iot_database.db"

def get_latest_data(limit=20):
    """Retrieve the latest sensor data from the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp, topic, message FROM sensor_data ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return []
