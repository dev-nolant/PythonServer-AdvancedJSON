from flask import Flask, render_template, jsonify, request
from os import walk
import json


data = open('databases/ParsedData_ignore.json', 'r').read()
data_dict = json.loads(data)

app = Flask(__name__)
@app.route("/", methods=['GET'])
def hello():
    user_count = len(data_dict)
    return render_template('index.html', user_count = user_count)

@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    return jsonify(data_dict)

@app.route('/api/v1/resources/users', methods=['GET'])
def api_id():

    methods = []
    if 'id' in request.args: id = (request.args['id']); methods.append('id')
    elif 'first_name' in request.args: first_name = str(request.args['first_name']); methods.append('first_name')
    else: return "Please provide a valid 'id' or 'first_name' or check the DOCS for help"
    
    results = []
    try:
        for user_data in data_dict:
            if user_data['id'] == int(id): results.append(user_data)
    except: print("No ID input, moving on."); pass
    try:
        for user_data in data_dict:
            if user_data['first_name'] == first_name: results.append(user_data)
    except: print("No Name input, moving on."); pass
    try:
        if len(results[0]) > 2: return jsonify(results)
        else: return jsonify(["ERROR: Arguments/Persons not found by method(s):{}".format(methods)])
    
    except IndexError: return jsonify(["ERROR: Arguments/Persons not found by method(s):{}".format(methods)])
    except Exception as e: return jsonify("ERROR: An unknown error has occured: {}".format(str(e)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6969, debug=True)





