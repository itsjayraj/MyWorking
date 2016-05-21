# This program needs a web-server on port 5000 with support for get /foo /bar with a delay of may be 1 second
# Run express server from D:\mongodb-training\nodejs-work

import socket
import time
from selectors34 import DefaultSelector, EVENT_READ, EVENT_WRITE

print("non-blocking socket with no real benifit in exec time");

selector = DefaultSelector()
n_tasks = 0


# Thr future class is responsible to hold and exec callbacks
class Future:
    def __init__(self):
        self.callbacks = []

    def resolve(self):
        for callback in self.callbacks:
            callback()


# Task class os responsible for calling next() on a generator
class Task:
    def __init__(self, gen):
        self.gen = gen
        self.step()

    def step(self):
        try:
            future = next(self.gen)
        except StopIteration:
            return
        future.callbacks.append(self.step)


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

    future = Future()
    selector.register(s.fileno(), EVENT_WRITE, data=future)

    # need to pause until s (socket) is writable
    yield future

    selector.unregister(s.fileno())
    s.send(request.encode())
    chunks = []

    while True:
        future = Future()
        selector.register(s.fileno(), EVENT_READ, data=future)
        yield future
        selector.unregister(s.fileno())
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            n_tasks -= 1
            return


start = time.time()
Task(get('/foo'))
Task(get('/bar'))
Task(get('/foo'))
Task(get('/bar'))
Task(get('/foo'))
Task(get('/bar'))
Task(get('/foo'))
Task(get('/bar'))
Task(get('/foo'))
Task(get('/bar'))

while n_tasks:
    events = selector.select()
    for event, mask in events:
        future = event.data
        future.resolve()

print('took %.1f sec' % (time.time() - start))
