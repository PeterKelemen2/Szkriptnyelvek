MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]

pelda = '''Példák
"ablak" → mély
"erkély" → magas
"kisvasút" → vegyes
"magas" → mély :)
"mély" → magas :)
"Pfffffff" → semmilyen'''


def hangrend(word_list):
    print("\nMegoldás:")
    for word in word_list:
        mely_word = 0
        magas_word = 0

        for char in word:
            if char in MELY_MGHK:
                mely_word += 1
            elif char in MAGAS_MGHK:
                magas_word += 1

        if mely_word > 0 and magas_word == 0:
            print('"' + word + '" → mély')
        elif magas_word > 0 and mely_word == 0:
            print('"' + word + '" → magas')
        elif magas_word > 0 and mely_word > 0:
            print('"' + word + '" → vegyes')
        else:
            print('"' + word + '" → semmilyen')


def main():
    print(pelda)
    hangrend(words)


if __name__ == "__main__":
    main()
