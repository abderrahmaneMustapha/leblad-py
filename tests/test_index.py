
import unittest
import json


from src import Api
from tests.test_cases_index import TestCases
class TestApi(unittest.TestCase):
    data = json.load(open("./data/WilayaList.json", encoding="utf-8"))
    test_cases = TestCases()
    api = Api()
    #def testLoop(self, test_cases, func):

    def test_getWilayaList(self):
        expected = [
            'Adrar', 'Chlef', 'Laghouat', 'Oum El Bouaghi', 'Batna', 'Béjaïa',
            'Biskra', 'Bechar', 'Blida', 'Bouira', 'Tamanrasset', 'Tbessa',
            'Tlemcen', 'Tiaret', 'Tizi Ouzou', 'Alger', 'Djelfa', 'Jijel',
            'Sétif', 'Saefda', 'Skikda', 'Sidi Bel Abbes', 'Annaba', 'Guelma',
            'Constantine', 'Medea', 'Mostaganem', "M'Sila", 'Mascara',
            'Ouargla', 'Oran', 'El Bayadh', 'Illizi', 'Bordj Bou Arreridj',
            'Boumerdes', 'El Tarf', 'Tindouf', 'Tissemsilt', 'El Oued',
            'Khenchela', 'Souk Ahras', 'Tipaza', 'Mila', 'Ain Defla', 'Naama',
            'Ain Temouchent', 'Ghardaïa', 'Relizane'
        ]
        tested_data = self.api.getWilayaList()
        self.assertEqual(len(tested_data),len(expected))
        self.assertEqual(tested_data,expected)

    def test_getWilayaByCode(self):
        test_cases = self.test_cases.test_cases_getWilayaByCode()
        for test_case in test_cases:
            tested_data = self.api.getWilayaByCode(test_case['input'])
            self.assertEqual(tested_data, test_case['expected'] )
    
    def test_getWilayaByZipCode(self):
        test_cases = self.test_cases.test_cases_getWilayaByZipCode()
        for test_case in test_cases:
            tested_data = self.api.getWilayaByZipCode(test_case['input'])
            self.assertEqual(tested_data, test_case['expected'] )

    def test_getBaladiyatsForDaira(self):
        test_cases = self.test_cases.test_cases_getBaladyiatsForDaira()
        for test_case in test_cases:
            tested_data = self.api.getBaladyiatsForDaira(test_case['input'])
            self.assertEqual(tested_data, test_case['expected'])

    def test_getBaladyiatsForWilaya(self):
        test_cases = self.test_cases.test_cases_getBaladyiatsForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getBaladyiatsForWilaya(test_case['input'])
            self.assertTrue(any(  elem in test_case['expected']  for elem in tested_data  ))

if __name__ == '__main__':
    unittest.main()