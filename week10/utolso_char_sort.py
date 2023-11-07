def first_letter(word):
    return word[0]


def last_letter(word):
    return word[-1]


def main():
    words = ['ccd', 'aaaa', 'd', 'bz']
    print(sorted(words, key=first_letter))
    print(sorted(words, key=last_letter))


if __name__ == '__main__':
    main()
