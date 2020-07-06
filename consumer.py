from kafka import KafkaConsumer

consumer = KafkaConsumer('test-topic', group_id='consumer-1', bootstrap_servers='0.0.0.0:9092')

for message in consumer:
	print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
