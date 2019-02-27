from flask import Flask, render_template

app = Flask(__name__, static_url_path='')


@app.errorhandler(404)
def not_found(e):
    return render_template('404_not_found.html'),404


@app.route('/index/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, host="localhost")
