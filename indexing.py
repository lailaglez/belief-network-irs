def create(keys, documents, VM):
    d = {}
    for ki in keys:
        d[ki] = {}
        for dj in documents:
            d[ki][dj] = VM.W(ki,dj)
    return d


def add(new_key, new_value):
    pass


def update(key, new_value):
    pass


def delete(key):
    pass


def get(key):
    pass