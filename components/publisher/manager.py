import json

from kafka_producer import Kafka_pruducer
from files_loader import get_the_data
from helpers import Cleaner

class Manager:
    def __init__(self):
        self.cleaner = Cleaner()

    def run(self):
        data = get_the_data(self)   # get the json files with the data
        data =data[0]
        cleand_data = self.normalize(data)
        self.build_producer_and_publish_message('localhost:9092',"interesting", {"data":cleand_data})




    def normalize(self ,data):
            cleand =  []
            cleand_data = self.cleaner.normalize_text(data)
            cleand.append(cleand_data)
            return cleand


    def build_producer_and_publish_message(self ,bootstrap_servers,topic,msg):
        producer = Kafka_pruducer(bootstrap_servers)
        producer.publish_message_with_key(topic,msg)


