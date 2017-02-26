from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'JavaScript'}, ]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)