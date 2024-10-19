import configparser
from flask import Flask

# Load configuration from the INI file
config = configparser.ConfigParser()
config.read('config.ini')

host = config['server']['host']
port = int(config['server']['port'])

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(host=host, port=port)
