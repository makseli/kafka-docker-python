import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='172.17.0.1:32774')

var = 1
while var == 1:

    num = random.randint(0, 10)

    num_bytes = bytes(str(num), encoding='utf-8')

    producer.send('test-topic', value=num_bytes, key=num_bytes)

    # wait 1 second
    time.sleep(1)
