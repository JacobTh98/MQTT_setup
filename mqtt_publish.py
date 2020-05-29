import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("Broker-Ip",1883,60)

client.publish("Deine Nachricht");

client.disconnect();
