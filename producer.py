import random
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='0.0.0.0:9092')

num = random.randint(0, 10)

num_bytes = bytes(str(num), encoding='utf-8')

is_send = producer.send('test-topic', value=num_bytes, key=num_bytes)
# Block for 'synchronous' sends
try:
    record_metadata = is_send.get(timeout=2)
    print(record_metadata)
except Exception as exc:
    # Decide what to do if produce request failed...
    #log.exception()
    print('Exception: ', exc)

print(' finish ')
# Successful result returns assigned partition and offset

# print(record_metadata.partition)
# print(record_metadata.offset)



