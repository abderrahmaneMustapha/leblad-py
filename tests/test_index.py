
import unittest
import json


from src import Api
class TestApi(unittest.TestCase):
    data = json.load(open("./data/WilayaList.json", encoding="utf-8"))

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
        tested_data = Api().getWilayaList()
        self.assertEqual(len(tested_data),len(expected))
        self.assertEqual(tested_data,expected)



if __name__ == '__main__':
    unittest.main()