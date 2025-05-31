from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)
ip_address = "10.14.3.8"
response = None

@app.route("/", methods=["GET", "POST"])
def home():
    global response
    if request.method == "POST":
        #target_ip = request.form.get("target_ip")
        message = request.form.get("message")
        response = response + "\n" + message
   
    return render_template("index.html",ip_address=ip_address, response=response)

#@app.route("/send_message", methods=["POST"])
#def send_message():
#    target_ip = request.form.get("target_ip")
#    message = request.form.get("message")
    
#    # For now, just return the data as a response
#    return jsonify({"target_ip": target_ip, "message": message})


if __name__ == "__main__":
    app.run(host=ip_address, port=5000)