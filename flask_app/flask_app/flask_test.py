import unittest
import json
import requests


class GeoTest(unittest.TestCase):
    """
    Just a quick unit test to compare results with expected results, mostly if we
    change the functions later on and want to confirm it works the same. Realistically,
    we would add more unit tests for more functionality.
    """

    def test_all(self):
        # This is our local host url, can change as needed
        url = "http://127.0.0.1:5000/padus"
        # Use LA geojson as test case
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
        with open("data/expected_results.json") as f:
            expected_results = json.load(f)
        self.assertEqual(expected_results, data)


if __name__ == '__main__':
    geo = GeoTest()
