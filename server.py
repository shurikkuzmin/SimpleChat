import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

server.bind(('localhost', 5555))
server.listen(1)

print("Server is listening for a connection...")

conn, addr = server.accept()

print(f"Connected by {addr}")

isRunning = True
while isRunning:
    data = conn.recv(1024).decode("utf-8")

    if data == "bye" or data == "quit":
        print("Bye!")
        isRunning = False

    print("Message from client: ", data)

    #data = conn.recv(1024).decode()
    #if not data or data.lower() == 'bye':
    #    print("Client disconnected.")
    #    break
    #print("Client:", data)
    #reply = input("You: ")
    #conn.sendall(reply.encode())
    #if reply.lower() == 'bye':
    #    break

conn.close()
socket.close()