from kafka import KafkaConsumer

consumer = KafkaConsumer('test-topic', group_id='consumer-1', bootstrap_servers='172.17.0.1:32774')

for message in consumer:
#	print(msg).encode('utf-8')
	print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
