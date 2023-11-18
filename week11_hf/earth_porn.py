import json
from pprint import pprint


def main():
    json_data = open("earth_porn.json", "r")
    json_deserialized = json.load(json_data)
    json_data.close()

    # pprint(json_deserialized)
    for i in range(0, 24):
        print("Image URL:", json_deserialized['data']['children'][i]['data']['preview']['images'][0]['source']['url'])
        print("Width:", json_deserialized['data']['children'][i]['data']['preview']['images'][0]['source']['width'])
        print("Height:", json_deserialized['data']['children'][i]['data']['preview']['images'][0]['source']['height'],
              '\n')


if __name__ == "__main__":
    main()
