from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
                return('INDEX PAGE')


if __name__ == '__main__':
        app.debug = True
        app.run()