import json
import requests

"""
Use this to generate expected outputs for the unit test, then we can assert they
match in case we change any of the functions later
"""
def generate(url):
    with open("data/la.geojson") as f:
        json_data = json.load(f)
    all_result = requests.get(url, json=json_data)
    manager_result = requests.get(url + "?type=manager", json=json_data)
    desig_result = requests.get(url + "?type=designation", json=json_data)
    feature_result = requests.get(url + "?type=feature", json=json_data)
    data = {
        "all_result": all_result.text,
        "manager_result": manager_result.text,
        "desig_result": desig_result.text,
        "feature_result": feature_result.text
    }
    with open('data/expected_results.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/padus"
    generate(url)
