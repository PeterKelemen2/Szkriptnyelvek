import json
from pprint import pprint


def main():
    f = open("person.json", "r")
    deserialized = json.load(f)
    f.close()

    print(type(deserialized))
    print(deserialized)  # Csak simán kiírja a dictionaryt
    pprint(deserialized)

    json_string = """{
  "last": "Doe",
  "first": "John",
  "age": 39,
  "sex": "M",
  "registered": true,
  "salary": 70000
}
"""
    print(json_string)

    other_d = json.loads(json_string)
    pprint(other_d)

    f = open("newPersonJSON.json", "w")
    json.dump(other_d, f, indent=4, sort_keys=True)
    f.close()

    print(json.dumps(other_d))  # Egy string


if __name__ == "__main__":
    main()
