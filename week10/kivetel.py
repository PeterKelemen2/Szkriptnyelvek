import sys


def cat(fname):
    try:
        f = open(fname, "r")
        text = f.read()
        print('---', fname, ':')
        print(text)
    except IOError as e:
        print("Error, file not found: ", fname, file=sys.stderr)
        print("Error message:", e)
    except:
        print("Error while reading the following file", fname, file=sys.stderr)
    else:
        print("No error")
    finally:
        # Bármi van, lefut
        f.close()
        print("End of file reading")


if __name__ == '__main__':
    args = sys.argv[1:]
    for arg in args:
        cat(arg)
