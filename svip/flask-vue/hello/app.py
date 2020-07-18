"""
app:
"""
# author: rexdu
# create: 2020/7/18 16:55

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def hello():
    users = {
        1: 'duqing',
        2: 'lifan',
        3: 'guoguo'
    }
    return jsonify(users=users)


if __name__ == '__main__':
    app.run()
