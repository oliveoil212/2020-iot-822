import paho.mqtt.client as mqtt
import mraa
import time
import random
# ******config***************
deviceId = "DH308jgQ"
deviceKey = "VL8zuKJTMQB27Caq"
HOST = "mqtt.mcs.mediatek.com"
PORT = 1883
ALIVETIME = 60
Device = "mcs/" + deviceId + "/" + deviceKey
Device_LED = "mcs/" + deviceId + "/" + deviceKey + "/ledControl"
Device_Temperature = "mcs/" + deviceId + "/" + deviceKey + "/Temperature"
Device_Humidity = "mcs/" + deviceId + "/" + deviceKey + "/Humidity"
#####################
# ********PIN************
Led = mraa.GPIO(44)
Led.dir(mraa.DIR_OUT)
# *******************connect
client = mqtt.Client()
client.connect(HOST)

#*******************
def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code "+str(rc))
    client.subscribe(Device_LED)
def on_publish(client, userdata, message):
    print("Post!")
def ledswitch(client, userdata, message):
    x = str(message.payload.decode("utf-8")).split(",")
    status = x[2]
    if status == "1":
        print("LED is ON")
        Led.write(1)
    else:
        print("LED is OFF")
        Led.write(0)

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
