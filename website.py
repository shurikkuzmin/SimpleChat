from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Flask Hello World application!"}

@app.route("/hello")
def hello():
    return {"new_message": "Privet!"}


if __name__ == "__main__":
    app.run(debug=True)