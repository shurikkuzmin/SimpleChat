import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

server.bind(('localhost', 5555))
server.listen(1)

print("Server is listening for a connection...")

conn, addr = server.accept()

print(f"Connected by {addr}")

while True:
    request = conn.recv(1024).decode("utf-8")

    if request == "bye" or request == "quit":
        print("Bye!")
        break

    print("Message from client: ", request)
    
    reply = input("Enter your message: ")
    conn.sendall(reply.encode("utf-8"))
    if reply == "bye" or reply == "quit":
        print("Bye!")
        break

conn.close()
server.close()