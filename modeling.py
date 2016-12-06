import os
import processing


# Este método manda a procesar los datos y crea un índice
def build(path):
    processing.process(path)
    # create index


# Este método realiza la query usando el índice generado
def query(s):
    success = False
    results = []
    return success, results