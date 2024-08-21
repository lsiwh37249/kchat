# kchat


### Dependency
![img2](https://img.shields.io/badge/kafka-2.8%20-brightgreen.svg)
```
pip install kafka-python == 2.0.2
``` 

### code
```
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer = lambda x:json.dumps(x).encode('utf-8')
)

start = time.time()
for i in range(10):
    data = {'str' :'value' + str(i)}
    producer.send('kchat',value = data)
    producer.flush()

end = time.time()
print("[DONE]:", end - start)
```
### output
```
{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```
