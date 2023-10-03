def main():
    d = {}
    # d = dict()
    # print(type(d))  # dict
    d['kulcs'] = 'ertek'
    d['a'] = 'alfa'
    d['b'] = 'beta'
    d['g'] = 'gamma'
    print(d)
    print(d['a'])
    print(d.get('b'))
    print(d.get('o', "Nincs ilyen kulcs"))  # None
    # print(d['f'])  # KeyError
    print('a' in d)
    d['a'] = 'alfaaaa'
    print(d['a'])

    print(d.keys())
    print(d.values())
    print(list(d.values()))

    for k in d.keys():
        print(f"kulcs: {k} - érték: {d[k]}")

    print(d.items())
    for k, v in d.items():
        print(f"{k} - {v}")

    print('beta' in d.values())

    print(d)
    del d['a']
    print(d)


if __name__ == '__main__':
    main()
