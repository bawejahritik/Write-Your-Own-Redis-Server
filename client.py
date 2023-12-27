import socket
import os

def createConnectionTCP(serverName, serverPort):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    return clientSocket

def main():
    
    clientSocket = createConnectionTCP("127.0.0.1", 6379)
    while True:
        sentence = input()
        clientSocket.send(sentence.encode())

if __name__ == "__main__":
    main()