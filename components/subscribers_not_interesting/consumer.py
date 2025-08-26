from kafka import KafkaConsumer
import json


class Consumer:
    @staticmethod
    def get_consumer_events(topic="interesting"):
        """return a KafkaConsumer object for iterating over events"""
        bootstrap_server = 'localhost:9092'
        return KafkaConsumer(topic,
                            group_id='my-group',
                            value_deserializer=lambda m: json.loads(m.decode('ascii')),
                            bootstrap_servers=[bootstrap_server],
                            consumer_timeout_ms=3000)  # timeout קצר יותר - 3 שניות