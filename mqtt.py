import paho.mqtt.client as mqtt

def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    clent.subscribe('ano/laneRoute/#')
    
def on_message(client,userdata,msg):
    print("get message : "+msg.topic+""+str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('corsserver','cors..//hg')
client.connect('180.169.235.194',11444,60)

client.loop_forever()
