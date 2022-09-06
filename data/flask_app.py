from flask import Flask

app = Flask(__name__)


@app.route("/home")
def hello():
    return "Hello World!"


@app.route("/hello/<name>")
def helo_name(name):
    return f"Hello {name}!"


@app.route("/user/<int:user_id>")
def hello_user_id(user_id):
    return f"Hello user with id {user_id}!"


@app.route("/height/<float:height>")
def height(height):
    return f"Hello user with height {height}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath: {subpath}"


app.run(debug=True)
