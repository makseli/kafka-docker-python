import random
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

num = random.randint(0, 10)

data = {'number': num}

is_send = producer.send('test-topic', value=data)
# Block for 'synchronous' sends
try:
    record_metadata = is_send.get(timeout=2)
    print('send DATA: ', data)
except Exception as exc:
    # Decide what to do if produce request failed...
    # log.exception()
    print('Exception: ', exc)

print(' finish ')
# Successful result returns assigned partition and offset

# print(record_metadata.partition)
# print(record_metadata.offset)
