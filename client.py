import socket

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(('localhost', 5555))

print("Connected to the server. Type 'bye' or 'quit' to exit.")

while True:
    request = input("Enter your message: ")
    client.sendall(request.encode("utf-8"))
    if request == "bye" or request == "quit":
        print("Bye!")
        break

    reply = client.recv(1024).decode("utf-8")
    print("Message from serve: ",reply)
    if reply == "bye" or reply == "quit":
        print("Bye")
        break

client.close()
