from kafka import KafkaProducer
import json

'''
 生产者demo
 向test主题中循环写入10条json数据
 注意事项：要写入json数据需加上value_serializer参数，如下代码
'''
producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    bootstrap_servers=['192.168.31.12:9092']
)
for i in range(10):
    data = {
        "name": "李四三",
        "age": 24,
        "gender": "男",
        "id": i
    }
    #print(data)
    producer.send('ls', data)
producer.close()
