from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def hello():
    result = main.get_data("TSLA")
    return result

@app.route('/snap')
def snap_data():
    result = main.get_data("SNAP")
    return result

if __name__ == '__main__':
    app.run(debug=True)
