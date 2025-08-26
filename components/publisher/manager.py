import json


from kafka import KafkaAdminClient
from kafka_producer import Kafka_pruducer
from files_loader import Loader

class Manager:

    def run(self):
        interesting_data = Loader.get_interesting_data()   # get the json files with the data
        not_interesting_data = Loader.get_not_interesting_data()
        self.build_producer_and_publish_message('localhost:9092',"interesting", interesting_data)
        self.build_producer_and_publish_message('localhost:9092',"not_interesting", not_interesting_data)

    def build_producer_and_publish_message(self ,bootstrap_servers,topic,msg):
        producer = Kafka_pruducer(bootstrap_servers)
        producer.publish_message(topic, msg)


m =Manager()
# admin =KafkaAdminClient(bootstrap_servers=['localhost:9092'])
# print(admin.list_topics())
m.run()
