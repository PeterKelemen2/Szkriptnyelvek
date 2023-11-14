import requests


def main():
    URL = "https://python.org"
    path = "C:\\Users\\student\\Downloads\\kep.png"
    r = requests.get(URL)
    print(type(r))
    print(r)  # Állapotkód
    print(r.text)


if __name__ == "__main__":
    main()
