from kafka import KafkaConsumer

var = 1
while var == 1:

    consumer = KafkaConsumer('test-topic',
                            group_id='consumer-1',
                            bootstrap_servers='172.17.0.1:32768')

    for msg in consumer:
        print (msg)
