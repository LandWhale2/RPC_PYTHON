from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('localhost',8000),
                        requestHandler=RequestHandler)as server:
    server.register_introspection_functions()

    server.register_function(pow)

    def runserver_django(x,y):
        output = os.popen('python manage.py runserver').read()
        print(output)
        return

    def stop_server_django():
        output = os.popen('').read()
        print(output)
        return

    server.serve_forever()