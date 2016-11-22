import modeling




# Se llama cuando se cambia el path en la UI
def build(path):
    modeling.build(path)


# Se llama cuando se realiza una query desde la UI, count es el número de resultados deseados
def query(query, count):
    return modeling.query(query, count)