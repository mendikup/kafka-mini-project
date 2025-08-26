import json


from kafka import KafkaAdminClient
from kafka_producer import Kafka_pruducer
from files_loader import get_the_data

class Manager:

    def run(self):
        data = get_the_data()        # get the json files with the data
        self.build_producer_and_publish_message('localhost:9092',"interesting", data)

    def build_producer_and_publish_message(self ,bootstrap_servers,topic,msg):
        producer = Kafka_pruducer(bootstrap_servers)
        producer.publish_message_with_key(topic,msg)


m =Manager()
# admin =KafkaAdminClient(bootstrap_servers=['localhost:9092'])
# print(admin.list_topics())
m.run()
