import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    msg=message.payload
    print(msg)
#You have to add the broker-Ip and the topic you want to subsctibe

subscribe.callback(on_message_print, "Your_topic", hostname="Your_Broker_Ip")


