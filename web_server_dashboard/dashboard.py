
from flask import Flask, request, send_from_directory, send_file

app = Flask(__name__, static_url_path='/')

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('', path)

@app.route('/')
def index():
    return send_file("index.html")

if __name__ == "__main__":
	app.run(threaded=True)
