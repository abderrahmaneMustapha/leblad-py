
import unittest
import json


from leblad import Api
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
            self.assertEqual(tested_data['mattricule'], test_case['expected']['mattricule'] )
    
    def test_getWilayaByZipCode(self):
        test_cases = self.test_cases.test_cases_getWilayaByZipCode()
        for test_case in test_cases:
        
            tested_data = self.api.getWilayaByZipCode(test_case['input'])
            self.assertEqual(tested_data['mattricule'], test_case['expected']['mattricule'] )

    def test_getBaladiyatsForDaira(self):
        test_cases = self.test_cases.test_cases_getBaladyiatsForDaira()
        for test_case in test_cases:
            tested_data = self.api.getBaladyiatsForDaira(test_case['input'])
            self.assertEqual(tested_data, test_case['expected'])

    def test_getBaladyiatsForWilaya(self):
        test_cases = self.test_cases.test_cases_getBaladyiatsForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getBaladyiatsForWilaya(test_case['input'])
            for tested_case_element in  test_case['expected'] :
                self.assertTrue(tested_case_element in tested_data)

    def test_getDairatsForWilaya(self):
        test_cases = self.test_cases.test_cases_getDairatsForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getDairatsForWilaya(test_case['input'])
            for tested_case_element in  test_case['expected'] :
                self.assertTrue(tested_case_element in tested_data)

    def test_getFirstPhoneCodeForWilaya(self):
        test_cases = self.test_cases.test_cases_getFirstPhoneCodeForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getFirstPhoneCodeForWilaya(test_case['input'])
            self.assertTrue(test_case['expected'] ==  tested_data)

    def test_getPhoneCodesForWilaya(self):
        test_cases = self.test_cases.test_cases_getPhoneCodesForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getPhoneCodesForWilaya(test_case['input'])
            self.assertTrue(test_case['expected'] ==  tested_data)

    def test_getWilayaByBaladyiaName(self):
        test_cases = self.test_cases.test_cases_getWilayaByBaladyiaName()
        for test_case in test_cases:
            tested_data = self.api.getWilayaByBaladyiaName(test_case['input'])
            self.assertTrue(test_case['expected'].lower() ==  tested_data['name'].lower())
    
    def test_getWilayaByDairaName(self):
        test_cases = self.test_cases.test_cases_getWilayaByDairaName()
        for test_case in test_cases:
            tested_data = self.api.getWilayaByDairaName(test_case['input'])['name']
            self.assertTrue(test_case['expected'] ==  tested_data)
    
    def test_getWilayasByPhoneCode(self):
        test_cases = self.test_cases.test_cases_getWilayasByPhoneCode()
        for test_case in test_cases:
            tested_data = self.api.getWilayasByPhoneCode(test_case['input'])
            self.assertTrue(test_case['expected'] ==  tested_data['name'])

    def test_getZipCodesForWilaya(self):
        test_cases = self.test_cases.test_cases_getZipCodesForWilaya()
        for test_case in test_cases:
            tested_data = self.api.getZipCodesForWilaya(test_case['input'])
            self.assertTrue(test_case['expected'] ==  tested_data)
    
    def test_getAdjacentWilaya(self):
        test_cases = self.test_cases.test_cases_getAdjacentWilaya()
        for test_case in test_cases:
            tested_data = self.api.getAdjacentWilaya(test_case['input'])
            self.assertTrue(test_case['expected'] ==  tested_data)
    
    def test_getFullAdjacentWilaya(self):
        test_cases = self.test_cases.test_cases_getAdjacentWilaya()
        for test_case in test_cases:
            tested_data = self.api.getFullAdjacentWilaya(test_case['input'])
            for element in tested_data:
                _ , value = next(iter(element.items()))
                self.assertTrue(value in  test_case['expected'])

if __name__ == '__main__':
    unittest.main()