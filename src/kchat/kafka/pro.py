from kafka import KafkaProducer
import time
import json
from tqdm import tqdm
producer = KafkaProducer(
    bootstrap_servers=['ec2-3-36-61-204.ap-northeast-2.compute.amazonaws.com:9092'],
    value_serializer = lambda x:json.dumps(x).encode('utf-8')
)

start = time.time()
for i in tqdm(range(10)):
    data = {'str' :'value' + str(i)}
    producer.send('kchat',value = data)
    producer.flush()
    time.sleep(1)

end = time.time()
print("[DONE]:", end - start)

