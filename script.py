import subprocess
import paho.mqtt.client as mqtt
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print("Topic:", msg.topic)
    payload = msg.payload.decode('utf-8', 'ignore')
    print(payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt.eclipse.org", 1883, 60)
client.subscribe("dse/monitor")
client.loop_start()

while(True):
  monitor = subprocess.check_output(['sh', 'monitor.sh'])
  client.publish("dse/monitor", monitor)
  sleep(8)