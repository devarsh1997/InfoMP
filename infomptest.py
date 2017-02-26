from flask import Flask, jsonify, json, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
with open('info_MP_unified.json') as data_file:

    jdata = json.load(data_file)
mp_data_unified = jdata

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'Welcome to InfoMP API!'})

@app.route('/infomp', methods=['GET'])
def returnAll():
    return jsonify({'mp_data_unified' : mp_data_unified})

@app.route('/infomp/<string:search>', methods=['GET'])
def returnOne(search):
    index = next(index for (index, d) in enumerate(mp_data_unified) if d["constituency"] == search)
    constituency = next((item for item in jdata if item.get("consituency") or item["constituency"] == search), "Invalid Constituency")
    return jsonify({"constituency": mp_data_unified[index]})

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app on port 5000 in debug mode