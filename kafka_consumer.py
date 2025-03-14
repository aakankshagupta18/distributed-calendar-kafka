from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer(
    'calendar_events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

conn = psycopg2.connect("dbname=calendar_db user=postgres password=secret")
cursor = conn.cursor()

def process_event(event):
    if event['action'] == 'create':
        cursor.execute(
            "INSERT INTO events (id, title, start_time, end_time) VALUES (%s, %s, %s, %s)",
            (event['event_id'], event['title'], event['start_time'], event['end_time'])
        )
    elif event['action'] == 'update':
        cursor.execute(
            "UPDATE events SET title=%s, start_time=%s, end_time=%s WHERE id=%s",
            (event['title'], event['start_time'], event['end_time'], event['event_id'])
        )
    elif event['action'] == 'delete':
        cursor.execute("DELETE FROM events WHERE id=%s", (event['event_id'],))
    
    conn.commit()

for message in consumer:
    print(message)
    process_event(message.value)
