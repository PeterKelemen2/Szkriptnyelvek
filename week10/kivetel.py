import sys


def cat(fname):
    try:
        f = open(fname, "r")
        text = f.read()
        print('---', fname, ':')
        print(text)
        f.close()
    except IOError:
        print("Error, file not found: ", fname, file=sys.stderr)
    except:
        print("Error while reading the following file", fname, file=sys.stderr)


if __name__ == '__main__':
    args = sys.argv[1:]
    for arg in args:
        cat(arg)
