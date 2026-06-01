import json
from confluent_kafka import Producer
from tpm.runtime.events.models import BaseEvent
from typing import Dict, Any


class KafkaEventProducer:
    def __init__(self, config: Dict[str, Any]):
        """
        config format: {'bootstrap.servers': 'localhost:9092'}
        """
        self.producer = Producer(config)

    def _delivery_report(self, err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def publish(self, topic: str, event: BaseEvent) -> None:
        payload = event.model_dump_json()
        self.producer.produce(
            topic,
            payload.encode("utf-8"),
            key=event.event_id.encode("utf-8"),
            callback=self._delivery_report,
        )
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()
