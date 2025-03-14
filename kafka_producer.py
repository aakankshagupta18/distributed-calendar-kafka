from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_event(event):
    producer.send('calendar_events', event)
    producer.flush()

# Example event
if __name__ == "__main__":
    event_data = {
        "event_id": 123,
        "title": "Meeting",
        "start_time": "2025-03-15T10:00:00",
        "end_time": "2025-03-15T11:00:00",
        "action": "create"
    }
    
    send_event(event_data)
    print("Event sent!")
