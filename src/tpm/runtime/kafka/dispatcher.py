from tpm.runtime.events.models import BaseEvent
from tpm.runtime.kafka.producer import KafkaEventProducer
from typing import Dict, Any


class EventDispatcher:
    """
    Abstrai o Kafka para uso interno da plataforma nos workflows de envio de eventos (CQRS).
    """

    def __init__(self, config: Dict[str, Any]):
        self.producer = KafkaEventProducer(config)

    def dispatch(self, topic: str, event: BaseEvent):
        self.producer.publish(topic, event)
