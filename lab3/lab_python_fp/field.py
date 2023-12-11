def field(elems, *args):
    assert len(args) > 0
    i1 = len(elems)
    j1 = len(args)
    for i in range(i1):
        for j in range(j1):
            if args[j] in elems[i] and args[j] is not None:
                yield elems[i][args[j]]


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    for el in field(goods, 'title'):
        print(el)
    print('\n')
    for el in field(goods, 'title', 'price'):
        print(el)
