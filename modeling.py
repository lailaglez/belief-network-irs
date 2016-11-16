import json
import os
import processing


def build(s):
    path = read_build_json(s)
    names = [name for name in os.listdir(path) if name.endswith('.pdf') or name.endswith('.txt')]
    for name in names:
        with open(name, 'rt') as f:
            data = f.read()
            terms = read_process_json(processing.process(data))
            # create index


def query(s):
    success = False
    results = []
    return generate_report_json(success, results)


def generate_report_json(success, results):
    dic = {'action': 'report', 'success': success, 'results': []}
    if success:
        dic[results] = [{'document':r[0], 'match': r[1]} for r in results]
    return dic


def read_build_json(s):
    return json.loads(s)['path']


def read_process_json(s):
    return json.loads(s)['terms']
