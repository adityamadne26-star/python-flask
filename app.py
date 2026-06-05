from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def home():
    return "Hello World"

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
