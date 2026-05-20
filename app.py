from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"

socketio = SocketIO(app)

# ---------- Home ----------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- Socket Events ----------
@socketio.on("message")
def handle_message(msg):
    send(msg, broadcast=True)

# ---------- Run ----------
if __name__ == "__main__":
    socketio.run(app, debug=True)
