from flask import Flask, render_template, request, jsonify
import socket
import requests

app = Flask(__name__)
ip_address = "10.14.3.8"
messages = None

@app.route("/", methods=["GET", "POST"])
def home():
    global messages
    if request.method == "POST":
        if request.form:
            print("Received form data")
            print(request.form)
            target_ip = request.form.get("target_ip")
            target_message = request.form.get("target_message")
            requests.post(f"http://{target_ip}:5000/receive", data={"message": target_message})
            print("Message sent to target IP:", target_ip)
   
    return render_template("index.html",ip_address=ip_address, messages=messages)

@app.route("/receive", methods=["POST"])
def receive():
    global messages
    message = request.data.get("message")
    if messages is None:
        messages = message
    else:
        messages += "\n" + message
    print("Received message:", message)
    return jsonify({"status": "success", "message": "Message received"}), 200

if __name__ == "__main__":
    app.run(host=ip_address, port=5000, threaded=True)