def first_letter(word):
    szam = word.split(':')
    return int(szam[0])


def last_column(row):
    szam = row[len(row) - 1]
    return szam


def main():
    data = [
        (1, 'Albany', 'NY', 162692),
        (121, 'Wyoming', 'NY', 8722),
        (3, 'Allegany', 'NY', 11986),
        (123, 'Yates', 'NY', 5094)
    ]
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(data, key=last_column))
    print(sorted(users, key=first_letter))


if __name__ == '__main__':
    main()
