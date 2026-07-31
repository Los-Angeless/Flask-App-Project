from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST", "mysql")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER", "root")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD", "root")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB", "devops")

mysql = MySQL(app)

@app.route("/")
def home():
    return "Flask + MySQL Application is Running!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
