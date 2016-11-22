import os
import processing


# Este método manda a procesar los datos y crea un índice
def build(path):
    names = [name for name in os.listdir(path) if name.endswith('.pdf') or name.endswith('.txt')]
    processed_data = []
    for name in names:
        with open(name, 'rt') as f:
            # terms será la lista de términos del pdf/txt una vez procesado (quitados los stop words, etc.)
            terms = processing.process(f)
            processed_data.append(terms)
    # create index


# Este método realiza la query usando el índice generado
def query(s):
    success = False
    results = []
    return success, results