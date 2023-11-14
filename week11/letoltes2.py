import urllib.request


def main():
    url = "https://www.python.org/static/img/python-logo-large.c36dccadd999.png"
    path = "C:\\Users\\student\\Downloads\\kep.png"

    urllib.request.urlretrieve(url, path)


if __name__ == "__main__":
    main()
