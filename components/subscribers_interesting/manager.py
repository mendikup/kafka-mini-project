import datetime
from consumer import Consumer
from dal import Dal
# from main import manager


class Manager:
    def __init__(self):
        self.dal = Dal()

    def consume(self):
        events = Consumer.get_consumer_events()
        all_messages = []

        for event in events:
            all_messages += event.value

        result = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": all_messages
        }

        if result['messages']:
            self.dal.insert_data(result)
            return {"status": "data has been inserted"}
        return {"msg": "there is no data to insert"}

    def get_all_data(self) -> list:
        return self.dal.get_all_data()

m =Manager()
m.consume()