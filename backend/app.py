from flask import Flask, jsonify

app = Flask(__name__)

userInfo=[
    {
        "name":"Rahul",
        "age":20
    },
    {
        "name":"Kidus",
        "age":22
    },
    {
        "name":"john",
        "age":23
    },
]




@app.route('/api/data')
def data():
    return jsonify({"userInfo":userInfo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
