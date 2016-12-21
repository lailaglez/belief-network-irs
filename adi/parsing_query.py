__author__ = 'Jose Gabriel'

import os
import pprint
import json
from adi.parsing_adi import read_block

def parse_query(s):
    d = {}
    with open(s) as f:
        line = f.readline()  # .I
        while line:
            query_number = int(line.strip().split()[-1])
            f.readline()
            query, line = read_block(f)
            d[query_number] = query

    return d

def parse_rel(qry, rel):
    d_qry = parse_query(qry)
    # pprint.pprint(d_qry)
    d = {}

    with open(rel) as f:
        for line in f.readlines():
            numbers = line.strip().split()
            q, doc_name = int(numbers[0]), "d%03d.txt" %(int(numbers[1]))
            text_query = d_qry[q]
            if text_query not in d:
                d[text_query] = []
            d[text_query].append(doc_name)

        # pprint.pprint(d)
    return d, d_qry

qry = "ADI.QRY"
rel = "ADI.REL"
d, d_qry = parse_rel(qry, rel)

s = json.dumps(d)
print(s)
with open('..' + os.sep + 'test_index' + os.sep + 'results.txt', 'w') as f:
    f.write(s)