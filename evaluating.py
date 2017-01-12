import math


def evaluate(relevant_documents, retrieved_documents):
    relevant_documents = set(relevant_documents)
    retrieved_documents = set(retrieved_documents)
    return {'precision': precision(relevant_documents, retrieved_documents),
            'recall': recall(relevant_documents, retrieved_documents),
            'f_measure': f_measure(relevant_documents, retrieved_documents),
            'e_measure': e_measure(relevant_documents, retrieved_documents)
            }


def precision(relevant_documents, retrieved_documents):
    if len(retrieved_documents) == 0:
        return 0
    retrieved_relevant_documents = relevant_documents.intersection(retrieved_documents)
    return len(retrieved_relevant_documents) / len(retrieved_documents)


def recall(relevant_documents, retrieved_documents):
    if len(retrieved_documents) == 0:
        return 0
    retrieved_relevant_documents = relevant_documents.intersection(retrieved_documents)
    return len(retrieved_relevant_documents) / len(relevant_documents)


def r_precision(relevant_documents, retrieved_documents, r):
    if len(retrieved_documents) == 0:
        return math.inf
    retrieved_relevant_documents = relevant_documents.intersection(set(retrieved_documents[:r]))
    return len(retrieved_relevant_documents) / len(retrieved_documents)


def f_measure(relevant_documents, retrieved_documents):
    p = precision(relevant_documents, retrieved_documents)
    r = recall(relevant_documents, retrieved_documents)
    if p + r == 0:
        return math.inf
    return 2 * p * r / (p + r)


def e_measure(relevant_documents, retrieved_documents, beta=1):
    p = precision(relevant_documents, retrieved_documents)
    r = recall(relevant_documents, retrieved_documents)
    if p + r == 0:
        return math.inf
    return (1 + beta ** 2) * p * r / (beta ** 2 * p + r)