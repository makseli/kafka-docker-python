import time
import random
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers='172.17.0.1:32768')

#var = 1
#while var == 1:

num = random.randint(0, 10)

num_bytes = bytes(str(num), encoding='utf-8')

is_send = producer.send('test-topic', value=num_bytes, key=num_bytes)
# Block for 'synchronous' sends
try:
    record_metadata = is_send.get(timeout=10)
except KafkaError as exc:
    # Decide what to do if produce request failed...
    #log.exception()
    print(exc)

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)


