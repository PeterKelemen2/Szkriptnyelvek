def read_strings():
    end_word = input("End word:")
    while True:
        current_word = input("Szo: ")
        if current_word == end_word:
            print("END")
            break
        else:
            print(str(string_info(current_word)) + "\n" + "-" * 20)


def string_info(word):
    info = {"upper": 0,
            "lower": 0,
            "length": len(word)}
    for c in word:
        if c == c.upper():
            info["upper"] += 1
        elif c == c.lower():
            info["lower"] += 1

    return info


def main():
    read_strings()


if __name__ == "__main__":
    main()
