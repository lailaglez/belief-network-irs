import modeling
import evaluating
import os
import json
import timeit
import math

def f():
    bn = modeling.BeliefNetwork()

    folder_path = '/media/laila/Storage/Escuela/5to Año/I Semestre/Sistemas de Información/Proyecto/test_index_adi'
    bn.build(folder_path, 'english')

    path = os.path.join(folder_path, 'results.json')
    with open(path) as f:
        dic = json.loads(f.read())
        p = 0
        r = 0
        e = 0
        f = 0
        n = len(dic)
        print(n)
        for k in dic:
            result, q = bn.query(k)
            print(k)
            print(q)
            result.sort(key=lambda t: t[1], reverse=True)
            result = result[:10]
            relevant = dic[k]
            print(relevant)
            print([r[0] for r in result])
            ev = evaluating.evaluate(relevant, [r[0] for r in result])
            p += ev['precision']
            r += ev['recall']
            if ev['f_measure'] != math.inf:
                f += ev['f_measure']
            if ev['e_measure'] != math.inf:
                e += ev['e_measure']
            print('--------------------------------------------------')
        print(p/n)
        print(r/n)
        print(e/n)
        print(f/n)
f()
# print(timeit.timeit(stmt=f, number=30)/30)
