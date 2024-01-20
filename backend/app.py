from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

main.get_data("TSLA")

if __name__ == '__main__':
    app.run(debug=True)
