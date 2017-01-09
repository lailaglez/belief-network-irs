__author__ = 'Jose Gabriel'

import os
import json
import sys
import pprint


def load_results(test_folder):
    try:
        with open(test_folder + os.sep + 'results.json') as f:
            return json.loads(f.read())
    except:
        print(
            "something was wrong, make sure that exists a file named \'results.json\' with the correct format in the test folder")


def report(test_folder):
    d = load_results(test_folder)
    for query, docs in d.items():
        model_docs = []  # model_docs debe ser la lista de documentos devueltos por nuestro modelo dada la consulta 'query'
        print("-----------------------QUERY------------------------")
        print(query)
        print("---------DOCUMETOS QUE DEBEN SER RECUPERADOS--------")
        print(docs)
        print("------DOCUMETOS RECUPERADOS POR NUESTRO MODELO------")
        print(model_docs)
        print("\n\n")


if __name__ == '__main__':
    test_folder = sys.argv[-1]
    report(test_folder)
