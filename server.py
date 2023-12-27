import socket
import time
import os

def createConnectionTCP(HOST, PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    return conn,s

def main():
    print("Starting redis server......")
    conn,s = createConnectionTCP("127.0.0.1" , 6379)
    while True:
        data = conn.recv(1024)
        print(data)

if __name__ == "__main__":
    main()