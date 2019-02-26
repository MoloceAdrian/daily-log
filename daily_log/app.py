from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return '<input type="text">'


if __name__ == "__main__":
    app.run(port = 8080, host="localhost")
