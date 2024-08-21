from kafka import KafkaConsumer
from json import loads

consumer =  KafkaConsumer(
        "kchat",
        bootstrap_servers=['localhost:9092'],
        value_deserializer = lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=15000,
        #auto_offset_reset='earliest',
        auto_offset_reset='latest', # 'earliest','latest'
        group_id="fbi",
        enable_auto_commit=True,

)

print('[Start] get consumer')
for m in consumer:
    print(f"topic={m.topic}, offset={m.offset} ")
print('[End] get consumer')

