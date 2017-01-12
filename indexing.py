import math


def create(documents, dictionary, VM):
    d = {}
    for dj in documents:
        for ki in dictionary[dj]:
            if ki not in d:
                d[ki]= {}
            d[ki][dj] = VM.Wq(ki, dj)
            if d[ki][dj] != 0:
                d[ki][dj] /= math.sqrt(sum([VM.Wq(kj, dj) ** 2 for kj in dictionary[dj]]))
    return d

#
# for ki in q:
#             if ki in self.Dictionary and dj in self.Dictionary[ki]:
#                     Pdk = self.VM.Wq(ki, dj) / math.sqrt(sum([self.VM.Wq(kj,dj) ** 2 for kj in self.Dictionary]))


def add(new_key, new_value):
    pass


def update(key, new_value):
    pass


def delete(key):
    pass


def get(key):
    pass