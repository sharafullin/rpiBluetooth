import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h1 style='color:red'>I am hosted on Raspberry Pi v4 !!!</h1></body></html>"

@app.route("/api/v1.0/test", methods=['GET'])
def api_get_test():
    return jsonify({'name':'test'});

@app.route("/api/v1.0/restart", methods=['GET'])
def api_get_restart():
    os.system('reboot')
    return jsonify({'name':'test'});

if __name__ == "__main__":
    app.run(host='0.0.0.0')
