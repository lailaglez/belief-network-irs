def evaluate(relevance_dict, documents_retrieved):
    return {'precision': precision(relevance_dict, documents_retrieved),
            'recall': recall(relevance_dict, documents_retrieved),
            'f_measure': f_measure(relevance_dict, documents_retrieved),
            'e_measure': e_measure(relevance_dict, documents_retrieved)
            }


def precision(relevance_dict, documents_retrieved):
    relevant_documents = set([d for d in relevance_dict if relevance_dict[d]])
    retrieved_relevant_document = relevant_documents.intersection(set(documents_retrieved))

    return len(retrieved_relevant_document) / len(documents_retrieved)


def recall(relevance_dict, documents_retrieved):
    relevant_documents = set([d for d in relevance_dict if relevance_dict[d]])
    retrieved_relevant_document = relevant_documents.intersection(set(documents_retrieved))

    return len(retrieved_relevant_document) / len(relevant_documents)


def r_precision(relevance_dict, documents_retrieved, r):
    relevant_documents = set([d for d in relevance_dict if relevance_dict[d]])
    retrieved_relevant_document = relevant_documents.intersection(set(documents_retrieved[:r]))

    return len(retrieved_relevant_document) / len(documents_retrieved)


def f_measure(relevance_dict, documents_retrieved):
    p = precision(relevance_dict, documents_retrieved)
    r = recall(relevance_dict, documents_retrieved)

    return 2 * p * r / (p + r)


def e_measure(relevance_dict, documents_retrieved, beta=1):
    p = precision(relevance_dict, documents_retrieved)
    r = recall(relevance_dict, documents_retrieved)

    return (1 + beta ** 2) * p * r / (beta ** 2 * p + r)