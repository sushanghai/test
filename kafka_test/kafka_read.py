from kafka import KafkaConsumer
import json

'''
    消费者demo
    消费test_lyl2主题中的数据
    注意事项：如需以json格式读取数据需加上value_deserializer参数
'''

consumer = KafkaConsumer('kafka', group_id="l22",
                         bootstrap_servers=['192.168.31.12:9092'],
                         auto_offset_reset='earliest', value_deserializer=json.loads
                         )
for message in consumer:
    print(message)
    #print(message.value)