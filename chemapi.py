from flask import Flask, jsonify, request
import json

app = Flask(__name__)
element_json = None
element_name_to_properties = {}

@app.route('/chemapi/', methods=['GET'])
def chemapi():
    return jsonify(element_json)

@app.route('/chemapi/groupblocks/', methods=['GET'])
def get_group_blocks():
    group_blocks = []
    for element in element_json:
        if element['groupBlock'] not in group_blocks:
            group_blocks.append(element['groupBlock'])
    return jsonify(group_blocks)

@app.route('/chemapi/atoms/<string:groupblock>', methods=['GET'])
def get_atoms_in_group_block(groupblock):
    parsed_groupblock_list = []
    starting_index = 0
    ending_index = 0
    for letter_index in range(0, len(groupblock)):
        if groupblock[letter_index].isupper() is True:
            ending_index = letter_index
        if starting_index != ending_index:
            parsed_groupblock_list.append(groupblock[starting_index:ending_index])
            starting_index = ending_index
    parsed_groupblock_list.append(groupblock[starting_index:])
    parsed_groupblock = ' '.join(parsed_groupblock_list).lower() 
    atoms = []
    for element in element_json:
        if element['groupBlock'] == parsed_groupblock:
            atoms.append(element['name'])
    return jsonify(atoms)

@app.route('/chemapi/<string:name>', methods=['GET'])
def get_atom_properties(name):
    if name.capitalize() in element_name_to_properties:
        return jsonify(element_name_to_properties[name.capitalize()])
    return "http 400"

@app.route('/chemapi/<string:name>/<string:property>', methods=['GET'])
def get_atom_atomic_number(name, property):
    atom_properties = element_name_to_properties[name.capitalize()]
    if property in atom_properties:
        return jsonify(atom_properties[property])
    return "http 400"

@app.route('/chemapi/atoms/', methods=['GET'])
def get_atom_names():
    atom_names = []
    for atom_index in element_json:
        atom_names.append(atom_index['name'])
    return jsonify(atom_names)

@app.route('/chemapi/symbols/', methods=['GET'])
def get_atom_symbols():
    atom_symbols = []
    for atom_index in element_json:
        atom_symbols.append(atom_index['symbol'])
    return jsonify(atom_symbols)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return chemapi()

def init_number_to_name_map():
    for i in range(0, len(element_json)):
        element_name_to_properties[element_json[i]['name']] = element_json[i]

if __name__ == '__main__':
    element_json_str = open('Elements.json', 'r').read()
    element_json = json.loads(element_json_str)
    if len(element_json_str) != 0:
        init_number_to_name_map()
        app.run(debug = True)
    else:
        print("File error.")