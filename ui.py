import json
import modeling


def build(path):
    modeling.build(generate_build_json(path))


def query(query, count):
    return modeling.query(generate_query_json(query, count))


def generate_build_json(path):
    return json.dumps({'action': 'build', 'path': path})


def generate_query_json(query, count):
    return json.dumps({'action': 'query', 'query': query, 'count': count})


def read_report_json(s):
    dic = json.loads(s)
    if dic['success']:
        return True, dic['results']
    return False, None