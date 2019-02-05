# Закодируйте любую строку из трех слов по алгоритму Хаффмана.


import string


def huffman(_vals):
    def assign(nodes, label, result, prefix=''):
        # print(nodes)
        childs = nodes[label]
        tree = {}

        if len(childs) == 2:
            tree['0'] = assign(nodes, childs[0], result, f'{prefix}0')
            tree['1'] = assign(nodes, childs[1], result, f'{prefix}1')
            # print(tree)
            return tree
        else:
            result[label] = prefix
            return label

    vals = _vals.copy()
    nodes = {}
    code = {}

    for n in vals.keys():
        nodes[n] = []

    while len(vals) > 1:
        s_vals = sorted(vals.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        vals[a1+a2] = vals.pop(a1) + vals.pop(a2)
        nodes[a1+a2] = [a1, a2]

    root = a1+a2
    tree = assign(nodes, root, code)
    return code, tree


vals = {v: i for i, v in enumerate(f'{string.ascii_lowercase} \'')}
code, tree = huffman(vals)
print(f'code:{code}\ntree:{tree}')

text = 'that\'s good course'
encoded = ''.join([code[t] for t in text])
print(encoded)

decoded = []
i = 0
while i < len(encoded):
    ch = encoded[i]
    act = tree[ch]

    while not isinstance(act, str):
        i += 1
        ch = encoded[i]
        act = act[ch]
    decoded.append(act)
    i += 1

print(''.join(decoded))