import xmlrpc.client
import time

server = xmlrpc.client.ServerProxy('http://192.168.0.117:9000')

count = 100

for i in range(count):
    time.sleep(1)
    response = server.message(i)
    print(response)

