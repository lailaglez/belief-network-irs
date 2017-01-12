import numpy as np
from numpy.linalg import norm


def retroalimentation(results, relevant, VM):
    new_scores = {}
    for r in results:
        new_scores[r[0]] = r[1]
        for rel in relevant:
            s = similarity(VM.documents_dictionary[r[0]], VM.documents_dictionary[rel])
            new_scores[r[0]] += s

    maximum = max(new_scores.values())
    known_relevant = [(k, v/maximum) for k, v in new_scores.items() if k in relevant]
    results = [(k, v/maximum) for k, v in new_scores.items() if k not in relevant]

    results.sort(key=lambda r: r[1], reverse=True)
    known_relevant.extend(results)

    return known_relevant


def similarity(d1, d2):
    s = set(d1[0]).union(set(d2[0]))
    v1 = []
    v2 = []
    for i in s:
        v1.append(d1[1].count(i))
        v2.append(d2[1].count(i))

    v1 = np.array(v1)
    v2 = np.array(v2)

    if norm(v1) == 0 or norm(v2) == 0:
        return 0
    return v1.dot(v2) / (norm(v1)*norm(v2))