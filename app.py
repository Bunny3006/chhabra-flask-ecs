from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return 'Hello from Chhabra ECS Container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
