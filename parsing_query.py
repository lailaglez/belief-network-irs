__author__ = 'Jose Gabriel'

import json
import os
import pprint
import json
from parsing_documents import read_block


def parse_query(s):
    d = {}
    with open(s) as f:
        line = f.readline()  # .I
        i = 1
        while line:
            # print(line)
            query_number = i #int(line.strip().split()[-1])
            f.readline()
            query, line = read_block(f)
            query = query.replace('?', '')
            query = query.replace('.', '')
            query = query.replace(',', '')
            query = query.replace('\n', '')
            d[query_number] = query.lower()
            i += 1

    return d


def parse_rel(qry, rel, out_folder):
    d_qry = parse_query(qry)
    # print(len(d_qry))
    d = {}

    with open(rel) as f:
        for line in f.readlines():
            numbers = line.strip().split()
            q, doc_name = int(numbers[0]), "d%03d.txt" % (int(numbers[1]))
            text_query = d_qry[q]
            if text_query not in d:
                d[text_query] = []
            d[text_query].append(doc_name)

            # pprint.pprint(d)

    s = json.dumps(d)
    with open(out_folder + os.sep + 'results.json', 'w') as f:
        f.write(s)


if __name__ == '__main__':
    qry = "adi" + os.sep + "ADI.QRY"
    rel = "adi" + os.sep + "ADI.REL"
    out_folder = "test_index"

    parse_rel(qry, rel)


