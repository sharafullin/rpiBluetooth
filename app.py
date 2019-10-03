from flask import Flask, jsonify

app = Flask(__name__)

payload = {'name':'test'}

@app.route("/")
def index():
    return "<html><body><h1 style='color:red'>I am hosted on Raspberry Pi !!!</h1></body></html>"

@app.route("/api/v1.0/test")
def api_get_test():
    return jsonify(payload);

if __name__ == "__main__":
    app.run(host='0.0.0.0')
