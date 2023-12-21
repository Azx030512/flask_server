import paho.mqtt.client as mqtt_client
import json
import logging
from database_connect import *

# 当连接成功时的回调函数


def on_connect(client, userdata, flags, rc):
    logging.debug("Connected with result code "+str(rc))
    logging.debug('userdata: '+str(userdata))
    logging.debug('flags: '+str(flags))
    # 订阅您感兴趣的主题
    for topic in userdata['subcriber_topic']:
        client.subscribe(topic)
        logging.info(f'subscribe to {topic}')


# 当收到消息时的回调函数
def on_message(client, userdata, msg):
    logging.debug(msg.topic+":"+str(msg.payload.decode()))
    iot_massage_json = json.loads(msg.payload.decode())
    iot_massage = IotMessage(**iot_massage_json)
    session.add(iot_massage)
    session.commit()


if __name__ == '__main__':

    # 创建 MQTT 客户端
    client = mqtt_client.Client()
    mqtt_data = {
        'subcriber_topic': ["testapp"]
    }
    client.user_data_set(mqtt_data)
    # 设置连接时的回调函数
    client.on_connect = on_connect

    # 设置收到消息时的回调函数
    client.on_message = on_message

    # 指定 MQTT 服务器的地址和端口号
    # 替换为您使用的 MQTT 服务器地址和端口号
    client.connect("127.0.0.1", 1883, 60)  # 将地址和端口替换为您的 MQTT 服务器地址和端口号

    # 在一个无限循环中保持连接，等待消息
    client.loop_forever()
