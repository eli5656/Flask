from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    username = request.args.get('username')
    return f"Hello {username}"


app.run(host="0.0.0.0")
