# import nltk
import json


def process(s):
    data = read_process_json(s)
    terms = []
    # f = nltk.load(data)
    # terms = nltk.tokenize(f)
    # terms = [word for word in terms if word not nltk.stopwordlist]
    # terms = nltk.stemming(terms)
    return generate_term_json(terms)


def generate_term_json(terms):
    return json.dumps({'terms': terms})


def read_process_json(s):
    return json.loads(s)['data']


