__author__ = 'Jose Gabriel'

import sys
import os
import parsing_documents
import parsing_query

if __name__ == '__main__':
    out_folder, docs, qry, rel = "", "", "", ""
    if len(sys.argv) == 0 or len(sys.argv) == 1:
        out_folder = 'test_index'
        docs = "adi" + os.sep + "ADI.ALL"
        qry = "adi" + os.sep + "ADI.QRY"
        rel = "adi" + os.sep + "ADI.REL"
    elif len(sys.argv) == 4 or len(sys.argv) == 5:
        dic = {'all': '', 'qry': '', 'rel': '', 'out_folder': ''}
        for i in sys.argv:
            ind = i.find("=")
            if ind != -1:
                dic[i[0:ind]] = i[ind + 1: len(i)]
        rel, qry, docs, out_folder = dic['rel'], dic['qry'], dic['all'], dic['out_folder']
        # print(docs)
    else:
        print("Missing parameters")

    try:  # averiguar como preguntar si una carpeta o fichero existe en python
        os.mkdir(out_folder)
    except FileExistsError:
        pass

    parsing_documents.parse_all(docs, out_folder)
    parsing_query.parse_rel(qry, rel, out_folder)
