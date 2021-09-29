from coapthon.server.coap import CoAP
from exampleresources import BasicResource
from coapthon.resources.resource import Resource
import random

path = "basic"
class NumResource(Resource):
    def __init__(self, name="NumResource", coap_server=None):
        super(NumResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = 0
        self.command = "nothing"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.edit_resource(request)
        print(self.payload)
        return self

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('basic/', BasicResource())
        self.add_resource('basic/', NumResource())


def main():
    server = CoAPServer("192.168.43.170", 5683)

    # BasicResource.payload = server.
    # server.add_resource('basic/',)
    try:
        server.listen(10)
        NumResource.payload = NumResource.render_GET(random.random,path)
        NumResource.render_PUT(NumResource.payload,path)
        NumResource.payload = NumResource.render_GET(" ",path)
        NumResource.render_PUT(NumResource.command,path)
    except KeyboardInterrupt:
        print ("Server Shutdown")
        server.close()
        print ("Exiting...")
    # print(server.receive_request())
    # server.send_datagram()
if __name__ == '__main__':
    main()