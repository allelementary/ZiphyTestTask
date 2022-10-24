expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]


def to_tree(data):
    sorted_source = sorted(data, key=lambda x: len(x[1]), reverse=True)
    result = {}
    for item in sorted_source:
        if item[0]:

            if item[0] in result:
                result[item[0]].update({item[1]: {}})

            else:
                result[item[0]] = {item[1]: {}}

            if item[1] in result:
                result[item[0]][item[1]].update(result[item[1]])
                result.pop(item[1])

    return result


assert to_tree(source) == expected
