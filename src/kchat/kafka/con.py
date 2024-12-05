from kafka import KafkaConsumer, TopicPartition
from json import loads
import os
OFFSET_FILE = 'consumer_offset.txt'

def save_offset(offset):
    with open(OFFSET_FILE, 'w') as f:
        f.write(str(offset))

def read_offset():
    if os.path.exists(OFFSET_FILE):
        with open(OFFSET_FILE, 'r') as f:
            return int(f.read().strip())
    return None

saved_offset = read_offset()
consumer =  KafkaConsumer(
    #"kchat",
    bootstrap_servers=['ec2-3-36-61-204.ap-northeast-2.compute.amazonaws.com:9092'],
    value_deserializer = lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=15000,
    auto_offset_reset='earliest',
    #auto_offset_reset='latest', # 'earliest','latest'
    #auto_offset_reset='earliest' if saved_offset is None else 'none',
    #group_id="fbi",
    enable_auto_commit=False,
)

print('[Start] get consumer')

p = TopicPartition('kchat', 0)
consumer.assign([p])

if saved_offset is not None:
    consumer.seek(p, saved_offset)
else:
    consumer.seek_to_beginning(p)
for m in consumer:
    print(f"offset={m.offset} value={m.value}")
    save_offset(m.offset+1)

print('[End] get consumer')

