import paho.mqtt.client as mqtt




client = mqtt.Client()
if client.connect('mqtt.eclipseprojects.io') == 0:
    print("connected  ")
   

while True:
  client.publish("TEMPERATURE", input('Message: '))
  

