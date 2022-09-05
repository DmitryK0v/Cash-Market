import unittest
import xmltodict
import requests

import models
import api


class ExternalTest(unittest.TestCase):
    def test_xml_api(self):
        r = requests.get("http://localhost:5000/api/xrates/xml")
        self.assertIn("<xrates>", r.text)
        print(r.text)
        xml_rates = xmltodict.parse(r.text)
        self.assertIn("xrates", xml_rates)
        self.assertIsInstance(xml_rates["xrates"]["xrate"], list)
        self.assertEqual(len(xml_rates["xrates"]["xrate"]), 3)

    def test_json_api(self):
        r = requests.get("http://localhost:5000/api/xrates/json")
        json_rates = r.json()
        self.assertIsInstance(json_rates, list)
        self.assertEqual(len(json_rates), 3)
        for rate in json_rates:
            self.assertIn("from", rate)
            self.assertIn("to", rate)
            self.assertIn("rate", rate)

    def test_json_api_uah(self):
        r = requests.get("http://localhost:5000/api/xrates/json?to_currency=980")
        json_rates = r.json()
        self.assertIsInstance(json_rates, list)
        self.assertEqual(len(json_rates), 2)


if __name__ == '__main__':
    unittest.main()
