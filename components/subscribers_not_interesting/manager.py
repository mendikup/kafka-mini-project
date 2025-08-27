import datetime
from consumer import Consumer
from dal import Dal


class Manager:
    def __init__(self):
        self.dal = Dal()

    def get_consume(self):

        consumer = Consumer.get_consumer_events()
        processed_count = 0

        try:
            for event in consumer:
                document = {
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "messages": event.value
                }
                if document['messages']:
                    self.dal.insert_data(document)
                    processed_count += 1

        except Exception as e:
            print(f"Consumer error: {e}")
        finally:
            try:
                # Ensure the consumer still "alive" before closing
                if consumer and hasattr(consumer, '_client'):
                    consumer.close()
            except Exception as e:
                print(f"Error closing consumer: {e}")

        return {"status": f"processed {processed_count} messages"}

    def get_all_data(self) -> list:
        return self.dal.get_all_data()

m = Manager()
print(m.get_consume())