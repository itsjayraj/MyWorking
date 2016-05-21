import socket

def main():
    host = "127.0.0.1"
    port = 5001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(2)
    c, addr  = s.accept()
    print "Connection from : " + str(addr)

    while True:
        data = c.recv(1024)
        if not data:
            break

        print("From connected user: " + str(data))
        print("sending ack")
        c.send("Msg Receoved from " + str(addr))

    c.close()

if __name__ == "__main__":
    main()