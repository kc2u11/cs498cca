from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    data = request.get_json()

    if 'num' in data:
        global seed_value
        seed_value += data['num']
        print(seed_value)

    return str(seed_value)

if __name__ == '__main__':
    app.run(debug=True)
