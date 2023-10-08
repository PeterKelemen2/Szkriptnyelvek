text = '''A katalán zászló, a Senyera színeit fogja viselni a következő 
idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes 
játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros 
csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, 
tekintettel a katalán önállósodási törekvésekre.'''

ekezetek = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
nem_ekezetek = "aeiooouuuAEIOOOUUU"


def main():
    """
    Remove diacritics (accents) from the input text by replacing characters with
    accents with their corresponding characters without accents.

    This function processes the 'text' variable and replaces characters with accents
    found in the 'ekezetek' string with their non-accented counterparts from the
    'nem_ekezetek' string. The result is printed to the console.

    Returns:
        None: This function does not return a value. It prints the modified text.
    """
    res = ""
    for c in range(len(text)):
        if text[c] in ekezetek:
            res += nem_ekezetek[ekezetek.index(text[c])]
        else:
            res += text[c]

    print(res)


if __name__ == "__main__":
    main()
