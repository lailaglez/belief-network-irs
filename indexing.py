import json


index = {}


def create(s):
    global index
    index = read_create_json(s)


def add(s):
    global index
    new_key_value_pair = read_add_json(s)
    index[new_key_value_pair[0]] = new_key_value_pair[1]


def update(s):
    add(s)


def delete(s):
    global index
    index.pop(read_delete_json(s))


def get(s):
    global index
    value = index.get(read_get_json(s), None)
    return generate_get_json(value is None, value)


def generate_get_json(success, value):
    return json.dumps({'success': success, 'value': value})


def read_create_json(s):
    data = json.loads(s)['data']
    return {d['key']: d['value'] for d in data}


def read_add_json(s):
    data = json.loads(s)
    return data['key'], data['value']


def read_update_json(s):
    return read_add_json(s)


def read_delete_json(s):
    return json.loads(s)['key']


def read_get_json(s):
    return json.loads(s)['key']
