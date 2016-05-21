# This program needs a web-server on port 5000 with support for get /foo /bar with a delay of may be 1 second
# Run express server from D:\mongodb-training\nodejs-work
import socket
import time
from selectors34 import DefaultSelector, EVENT_READ, EVENT_WRITE

print("non-blocking socket with no real benifit in exec time");

selector = DefaultSelector()
def get(path):
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 3000))
    except:
        pass

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    selector.unregister(s.fileno())
    s.send(request.encode())
    chunks = []
    while True:
        selector.register(s.fileno(), EVENT_READ)
        selector.select()
        selector.unregister(s.fileno())
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            return

start = time.time()
get('/foo')
get('/foo')
get('/foo')
get('/foo')
get('/foo')
get('/foo')

print('took %.1f sec' % (time.time() - start))
