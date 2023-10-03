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


if __name__ == '__main__':
    main()
