import modeling
import evaluating
import retroalimentation
import os
import json
import math

def f():
    bn = modeling.BeliefNetwork()

    folder_path = '/media/laila/Storage/Escuela/5to Año/I Semestre/Sistemas de Información/Proyecto/test_index_adi'
    bn.build(folder_path, 'english')

    path = os.path.join(folder_path, 'results.json')
    with open(path) as f:
        dic = json.loads(f.read())
        p1 = 0
        r1 = 0
        e1 = 0
        f1 = 0
        p2 = 0
        r2 = 0
        e2 = 0
        f2 = 0
        p3 = 0
        r3 = 0
        e3 = 0
        f3 = 0
        n = len(dic)
        for k in dic:
            print(k)
            result, q = bn.query(k)
            result.sort(key=lambda t: t[1], reverse=True)
            original_result = result
            result = result[:10]
            relevant = dic[k]

            ev = evaluating.evaluate(relevant, [r[0] for r in result])
            p1 += ev['precision']
            r1 += ev['recall']
            if ev['f_measure'] != math.inf:
                f1 += ev['f_measure']
            if ev['e_measure'] != math.inf:
                e1 += ev['e_measure']
            # print(result)
            # print(relevant)
            # print(ev)

            retr = retroalimentation.retroalimentation(original_result, relevant, bn)
            ev = evaluating.evaluate(relevant, [r[0] for r in retr][:10])
            p2 += ev['precision']
            r2 += ev['recall']
            if ev['f_measure'] != math.inf:
                f2 += ev['f_measure']
            if ev['e_measure'] != math.inf:
                e2 += ev['e_measure']
            # print(retr)
            # print(ev)

            retr = retroalimentation.retroalimentation(retr, relevant, bn)
            ev = evaluating.evaluate(relevant, [r[0] for r in retr][:10])
            p3 += ev['precision']
            r3 += ev['recall']
            if ev['f_measure'] != math.inf:
                f3 += ev['f_measure']
            if ev['e_measure'] != math.inf:
                e3 += ev['e_measure']
            # print(ev)
        print(p1/n)
        print(r1/n)
        print(e1/n)
        print(f1/n)
        print('--------------------------------------')
        print(p2/n)
        print(r2/n)
        print(e2/n)
        print(f2/n)
        print('--------------------------------------')
        print(p3/n)
        print(r3/n)
        print(e3/n)
        print(f3/n)

f()
