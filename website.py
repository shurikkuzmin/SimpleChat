from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/server")
def server():
    ip_address = '10.14.3.6'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

    server.bind((ip_address, port))
    server.listen(1)

    return render_template("server.html", ip_address=ip_address, port=port)

@app.route("/client")
def client():
    return render_template("client.html")

if __name__ == "__main__":
    app.run(debug=True)