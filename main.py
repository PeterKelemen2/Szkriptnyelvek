message = '''Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
'''

def decrypt(mes):
    result = ""
    for c in mes:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            ascii_value = ord(c)
            if ('a' <= c < 'y') or ('A' <= c < 'Y'):
                ascii_value += 2
            if (c == 'y' or c == 'z') or (c == 'Y' or c == 'Z'):
                ascii_value -= 24
            result += chr(ascii_value)
        else:
            result += c
    print(result)


def main():
    decrypt(message)

if __name__ == '__main__':
    main()
