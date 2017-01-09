__author__ = 'Jose Gabriel'

import os
import json
import sys
import pprint

test_folder = "test_index"


def load_results(folder_path, query):
    path = os.path.join(folder_path, 'results.json')
    try:
        with open(path) as f:
            dic = json.loads(f.read())
            return dic[query.lower()]
    except:
        return None


def report():
    d = load_results()
    for query, docs in d.items():
        model_docs = [] # model_docs debe ser la lista de documentos devueltos por nuestro modelo dada la consulta 'query'
        print("-----------------------QUERY------------------------")
        print(query)
        print("---------DOCUMETOS QUE DEBEN SER RECUPERADOS--------")
        print(docs)
        print("------DOCUMETOS RECUPERADOS POR NUESTRO MODELO------")
        print(model_docs)
        print("\n\n")


if __name__ == '__main__':
    report()