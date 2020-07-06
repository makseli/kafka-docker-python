from json import loads
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['0.0.0.0:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-json-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
