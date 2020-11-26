#python
import json

#utils
from  utils import GetBaladiyatsFromWilayaObject

class Api:
    data = json.load(open("../../data/WilayaList.json", encoding="utf-8"))
    
    def getWilayaList(self):
        wilaya_list = [ d["name"] for d in self.data ]
        return  wilaya_list
        
    def getWilayaByCode(self,  wilaya_code):
        def search(_data, wilaya_code):
            return list(filter(lambda i :  i["mattricule"] == wilaya_code, _data))
        return search(self.data, wilaya_code)[0]
    
    def getWilayaByZipCode(self, zip_code):
        def search(_data, wilaya_code):
            return list(filter(lambda i :  int(wilaya_code) in   i['postalCodes'], _data))
        return search(self.data, zip_code)[0]

    def getBaladyiatsForDaira(self, daira):
        for element in self.data:
            baladiyats, hasGivenDairaName = GetBaladiyatsFromWilayaObject(element["dairats"], daira)
            if hasGivenDairaName:
                return baladiyats

    def getBaladyiatsForWilaya(self, wilaya):
        baladiyats_list = []
        for element in self.data:
            baladiyats, hasGivenDairaName = GetBaladiyatsFromWilayaObject(element["dairats"], wilaya)
            if hasGivenDairaName:
                baladiyats_list.extend(baladiyats)

        return baladiyats_list

a  =  Api()


