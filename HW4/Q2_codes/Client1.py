from coapthon.client.helperclient import HelperClient
import random
import serial
from time import sleep

host = "192.168.43.178"
port = 5683
path ="basic"

client = HelperClient(server=(host, port))
data = str(int((random.random()*100)))
print("random number is : " )
print(data)
client.put(path, data)
sleep(15)
response = client.get(path)
command = response.payload
print("command is : ")
print(command)
client.stop()