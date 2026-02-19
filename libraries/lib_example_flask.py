from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def my_handler():
    return "Hello, World!"

if __name__ == "__main__":
    my_app.run(host = "0.0.0.0", port=8765)