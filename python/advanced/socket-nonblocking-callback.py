# This program needs a web-server on port 5000 with support for get /foo /bar with a delay of may be 1 second
# Run express server from D:\mongodb-training\nodejs-work

import socket
import time
from selectors34 import DefaultSelector, EVENT_READ, EVENT_WRITE

print("non-blocking socket with no real benifit in exec time");

selector = DefaultSelector()
n_tasks = 0

def get(path):
    global n_tasks
    n_tasks += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 3000))
    except:
        pass

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    callback = lambda: connected(s, request)
    selector.register(s.fileno(), EVENT_WRITE, data=callback)


def connected(s, request):
    selector.unregister(s.fileno())
    s.send(request.encode())
    chunks = []
    callback = lambda: readable(s, chunks)
    selector.register(s.fileno(), EVENT_READ, data=callback)


def readable(s, chunks):
    global n_tasks
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        callback = lambda: readable(s, chunks)
        selector.register(s.fileno(), EVENT_READ, data=callback)
    else:
        body = (b''.join(chunks)).decode()
        print(body.split('\n')[0])
        n_tasks -= 1


start = time.time()
get('/foo')
get('/bar')
get('/foo')
get('/bar')
get('/foo')
get('/bar')
get('/foo')
get('/bar')
get('/foo')
get('/bar')


while n_tasks:
    events = selector.select()
    for event, mask in events:
        cb = event.data
        cb()

print('took %.1f sec' % (time.time() - start))
