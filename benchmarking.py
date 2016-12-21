__author__ = 'Jose Gabriel'

import os
import json
import pprint

test_folder = "test_index"


def load_results():
    try:
        with open(test_folder + os.sep + 'results.json') as f:
            return json.loads(f.read())
    except:
        print("something was wrong, make sure that exists a file named \'results.json\' with the correct format in the test folder")


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