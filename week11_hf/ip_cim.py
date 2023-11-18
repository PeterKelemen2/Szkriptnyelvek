import json
from pprint import pprint

import requests


def main():
    ip_link = "http://jsonip.com/"
    r = requests.get(ip_link)

    d_json = json.loads(r.text)
    print("Az Ön IP címe:", d_json['ip'])


if __name__ == "__main__":
    main()
