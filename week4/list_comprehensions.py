lc1_list = ['auto', 'villamos', 'metro']
lc2_list = ['aladar', 'bela', 'cecil']
lc5_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
lc7_string = "The quick brown fox jumps over the lazy dog"
lc8_string = "python is an awesome language"
lc14_string = [' apple ', ' banana ', ' kiwi']
lc15_list = [1, 0, 1, 1, 0, 1, 0, 0]


def lc1(word_list):
    res = [word.upper() + "!" for word in word_list]
    print(res)
    return res


def lc2(word_list):
    res = [word[0].upper() + word[1:] for word in word_list]
    print(res)
    return res


def lc3():
    res = [0 for i in range(0, 10 + 1)]
    print(res)
    return res


def lc4():
    res = [i * 2 for i in range(1, 10 + 1)]
    print(res)
    return res


def lc5(word_list):
    res = [int(word) for word in word_list]
    print(res)
    return res


def lc6():
    s = "1234567"
    res_list = list(s)
    res = [int(char) for char in res_list]
    print(res)
    return res


def lc7(s):
    aux = list(s.split(" "))
    words_len = [len(word) for word in aux]
    print(words_len)
    return words_len


def lc8(s):
    aux = list(s.split(" "))
    first_chars = [word[0] for word in aux]
    print(first_chars)
    return first_chars


def lc9(s):
    aux = list(s.split(" "))
    words_len = [(word, len(word)) for word in aux]
    print(words_len)
    return words_len


def lc10():
    res = [n for n in range(10) if n % 2 == 0]
    print(res)
    return res


def lc11():
    res = [n * n for n in range(20) if (n * n) % 2 == 0]
    print(res)
    return res


def lc12():
    res = [n * n for n in range(20) if (n * n) % 10 == 4]
    print(res)
    return res


def lc13():
    res = [chr(i) for i in range(65, 90 + 1)]
    res = ''.join(res)
    print(res)
    return res


def lc14(word_list):
    res = [word.strip() for word in word_list]
    print(res)
    return res


def lc15(num_list):
    res = [str(num) for num in num_list]
    res = ''.join(res)
    print(res)
    return res


def main():
    lc1(lc1_list)
    lc2(lc2_list)
    lc3()
    lc4()
    lc5(lc5_list)
    lc6()
    lc7(lc7_string)
    lc8(lc8_string)
    lc9(lc7_string)
    lc10()
    lc11()
    lc12()
    lc13()
    lc14(lc14_string)
    lc15(lc15_list)


if __name__ == "__main__":
    main()
