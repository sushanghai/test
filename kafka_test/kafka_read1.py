from kafka import KafkaConsumer
import json
import os
import sqlite3

"""
创建数据库名称，配置Kafka的IP,group_id,topicl及转换
"""
db_filename = 'kafka_test.db'
server_list='192.168.31.12:9092'
topic ='ls'
group_id ='f3331bb323r22'


def sqlite3_db_create():
    try:
        #os.unlink(db_filename)
        if not os.path.exists(db_filename):
            conn = sqlite3.connect(db_filename)
            c = conn.cursor()
            c.execute('''create table kafka_table (id varchar (200),name varchar (200),gender varchar (200),age varchar (200))''')
            conn.commit()
            conn.close()
        else:
            pass
    except Exception as e:
        print(e)

def kafka_read():
    count = 0
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    consumer = KafkaConsumer(topic, group_id=group_id, auto_offset_reset='earliest', bootstrap_servers=server_list,
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    # print(consumer)
    for message in consumer:
        #print("%s:%d:%d: key=%s value=%s " % (message.topic, message.partition,message.offset, message.key,message.value)
        message_dict=message.value
        #for key,value in message_dict.items():
            #print("message_dict[%s]" %key,value)
        sql_name=message_dict['name']
        sql_age=message_dict['age']
        sql_gender =message_dict['gender']
        sql_id = message_dict['id']

        #print(id,name,gender,age)
        sql = '''insert into kafka_table (id,name,gender,age) values (?,?,?,?) '''
        sql_in = (sql_id,sql_name,sql_gender,sql_age)
        print(sql,sql_in)
        cursor.execute(sql,sql_in)
        conn.commit()
        count +=1
    print(count)
if __name__ == '__main__':
    sqlite3_db_create()
    kafka_read()

