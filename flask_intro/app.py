from flask import Flask

# Windows ==> set FLASK_APP="app.py"
# Linux ==> export FLASH_APP="app.py"

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/hi/<name>")
def say_hi_name(name):
    return f"Hi {name}!"


if __name__ == "__main__":
    app.run( )