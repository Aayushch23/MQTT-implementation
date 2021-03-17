import paho.mqtt.client as mqtt



def onMessage(client, userdata, message):
    print("Received message: " + message.payload.decode())


   

client = mqtt.Client()
if client.connect('mqtt.eclipseprojects.io') ==0 : 
  print("connected   use ctrl + C to terminate") 


client.subscribe("TEMPERATURE")
client.on_message = onMessage
client.loop_forever()

