There are three files in zip folder
1. publisher.py
2. subscriber.py
3.broker.py

Intruction on how to setup,compile and run
1. Use python 3.7 version for running python files
2.Run publisher file on a console/machine and simutanesouly run subscriber file on another console/machine
3. Don't use TCD wifi on any machine(maybe some security reasons) . I used my mobile network and it was working
4. When connected will appear on respect consoles
5. Whatever data you will enter in publisher console will appear on subscriber console as I have demonstrated in my video
6. For first test i have used a online broker link to online broker:- https://mqtt.eclipseprojects.io

7. For my second test i coded my own broker 
8. Change client.connect('mqtt.eclipseprojects.io') in publisher and subcriber file to client.connect('localhost',9999)
9. Now in same machine and different consoles run broker , publisher and subscriber file in there respective order
10. 3 message you should look for in broker console :-
      (i) "INFO :: hbmqtt.broker :: Listener 'default' bind to localhost:9999 (max_connections=-1)" for broker
      (ii)"INFO :: hbmqtt.broker :: Listener 'default': 1 connections acquired" for publisher is connected
      (iii) INFO :: hbmqtt.broker :: Listener 'default': 2 connections acquired" for subcriber is connected
10. Now mesaage sent by publisher file will appear on subscriber

You can transmit any message over MQTT protocol 