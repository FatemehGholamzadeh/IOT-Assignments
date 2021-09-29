from coapthon.client.helperclient import HelperClient

host = "192.168.43.178"
port = 5683
path ="basic"

client = HelperClient(server=(host, port))
response = client.get(path)
num = response.payload
print(num)
if  int(num)%2 == 0 :
    print("on")
    client.put(path,"on")
else:
    print("off")
    client.put(path,"off")
client.stop()