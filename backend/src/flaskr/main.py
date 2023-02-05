from flask import Flask
import os

app = Flask(__name__)
os.environ["FLASK_DEBUG"] = "1"


@app.route("/")
def root_path():
    return {"message": "Welcome to the shopping list backend"}


@app.route("/api/v1/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=8080)
