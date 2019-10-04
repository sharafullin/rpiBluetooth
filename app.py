from flask import Flask, jsonify
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import sqlite3

app = Flask(__name__)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

@app.route("/")
def index():
    return "<html><body><h1 style='color:red'>I am hosted on Raspberry Pi !!!</h1></body></html>"

@app.route("/api/v1.0/test", methods=['GET'])
def api_get_test():
    return jsonify({'name':'test'});

@app.route("/api/v1.0/restart", methods=['GET'])
def api_get_restart():
    publish.single("paho/restart", "0", hostname="localhost")
    return jsonify({'name':'test'});

if __name__ == "__main__":
    app.run(host='0.0.0.0')
