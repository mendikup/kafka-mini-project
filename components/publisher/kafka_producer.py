from kafka import KafkaProducer
import json


class Kafka_pruducer:

    def __init__(self, bootstrap_servers: str):
        self._producer = KafkaProducer(
            bootstrap_servers=[bootstrap_servers],
            value_serializer=lambda x:
            json.dumps(x).encode('utf-8'))
        print(self._producer.config)

    def publish_message(self, topic, messages):
        """
        :param topic: The topic to which the message will be published
        :param message: The event message
        :return: None
        """
        for category, data in messages.items():
            atrticles = data
            message = atrticles.pop()
            self._producer.send(topic, value=message)

    def flush(self):
        self._producer.flush()

    def close(self):
        self._producer.close()