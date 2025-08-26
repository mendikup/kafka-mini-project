import datetime
from consumer import Consumer
from dal import Dal
# from main import manager


class Manager:
    def __init__(self):
        self.dal = Dal()

    def get_consume(self):
        events = Consumer.get_consumer_events()
        messages = []

        for event in events:
            messages += event.value

        result = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "messages": messages
        }

        if result['messages']:
            self.dal.insert_data(result)
            return {"status": "data has been inserted"}
        return {"status": "there is no data to insert"}

    def get_all_data(self) -> list:
        return self.dal.get_all_data()

m =Manager()
m.get_consume()