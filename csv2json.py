def setdefault(d, k, c):
    d['size'] = 0
    cs = d.setdefault('children', [])
    cs1 = [x for x in cs if x['name'] == k]
    if cs1 == []:
        d1 = {'name': k, 'size': 1, 'color': c, 'text': 'black'}
        cs.append(d1)
        return d1
    else:
        return cs1[0]

colors = [{},{}]
with open('colors.csv') as f:
    for line in f:
        [k,c0,c1] = [x.strip() for x in line.split(',')]
        colors[0][k] = c0
        colors[1][k] = c1

d0 = {'name': 'Feelings'}
with open('feelings.csv') as f:
    for line in f:
        ks = [x.strip() for x in line.split(',')]
        i = 0
        k0 = ks[0]
        d = d0
        for k in ks:
            d = setdefault(d, k, colors[i % 2][k0])
            i += 1

import json
print(json.dumps(d0, indent = 4))
