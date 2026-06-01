import json
from confluent_kafka import Consumer, KafkaError, KafkaException
from typing import Dict, Any, Callable


class KafkaEventConsumer:
    def __init__(self, config: Dict[str, Any], topics: list[str]):
        """
        config format: {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'tpm_group',
            'auto.offset.reset': 'earliest'
        }
        """
        self.consumer = Consumer(config)
        self.consumer.subscribe(topics)

    def start_consuming(
        self, message_handler: Callable[[Dict[str, Any]], None]
    ) -> None:
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        raise KafkaException(msg.error())

                payload_str = msg.value().decode("utf-8")
                event_data = json.loads(payload_str)
                message_handler(event_data)

        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
