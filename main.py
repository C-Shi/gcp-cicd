from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Python Flask World docker cloud run v1.0 with auto trigger"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

