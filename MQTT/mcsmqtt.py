import paho.mqtt.client as mqtt
import random
import time
## http://www.steves-internet-guide.com/into-mqtt-python-client/
# ******config***************
deviceId = "DH308jgQ"
deviceKey = "VL8zuKJTMQB27Caq"
HOST = "mqtt.mcs.mediatek.com"
PORT = 1883
ALIVETIME = 60
# ALL_TOPIC = "mcs/" + deviceId + "/" + deviceKey + "/+"
Device = "mcs/" + deviceId + "/" + deviceKey
Device_LED = "mcs/" + deviceId + "/" + deviceKey + "/ledControl"
Device_Temperature = "mcs/" + deviceId + "/" + deviceKey + "/Temperature"
Device_Humidity = "mcs/" + deviceId + "/" + deviceKey + "/Humidity"

# *******************connect
client = mqtt.Client()
client.connect(HOST)

#*******************
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    # client.subscribe(Device + "/+")
    client.subscribe(Device_LED)
def on_publish(client, userdata, message):
    print("Post!")
# def on_message(client, userdata, message):
#     print("message topic=",message.topic)
#     print("message received " ,str(message.payload.decode("utf-8")))
def ledswitch(client, userdata, message):
    x = str(message.payload.decode("utf-8")).split(",")
    # print("message received ", x)
    status = x[2]
    if status == "1":
        print("Turn on Led")
    else:
        print("Turn off Led")

client.on_publish = on_publish
client.on_connect = on_connect
# client.on_message = on_message
client.message_callback_add(Device_LED, ledswitch)

client.loop_start()
while True:
    T = random.randint(0,30)
    H = random.randint(0,100)
    client.publish(Device_Temperature,",," + str(T))
    client.publish(Device_Humidity,",," + str(H))
    time.sleep(10)

