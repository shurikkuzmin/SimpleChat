from flask import Flask, render_template
import socket

app = Flask(__name__)
ip_address = "10.14.3.8"

@app.route("/")
def home():
    return render_template("index.html",ip_address=ip_address)

if __name__ == "__main__":
    app.run(host=ip_address, port=5000)