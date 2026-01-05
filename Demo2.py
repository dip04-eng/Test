from flask import Flask, jsonify
import os

app = Flask(__name__)

# ✅ Safe default value
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///local.db")

@app.route("/health")
def health():
    return "OK", 200

@app.route("/users")
def get_users():
    return jsonify({
        "db": DATABASE_URL,
        "users": ["Alice", "Bob", "Charlie"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)