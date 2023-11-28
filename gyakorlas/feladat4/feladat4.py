# HTML elemet regurális kifejezéssel lehet kiszedni - fólia

import requests
import re  # Reguláris kifejezés
import json


def main():
    r = requests.get("https://suvicsabika.github.io/")
    html = r.text

    tag = re.search(r"<h2>.*</h2>", html).group()[4:-5]
    print("Tag:", tag)
    motto = tag.split(": ")[1]
    print("Motto:", motto)

    d = {"motto": motto}

    with open("napi_motto.json", "w", encoding="utf-8") as f:
        json.dump(d, f)  # Kiírja fileba


if __name__ == "__main__":
    main()
