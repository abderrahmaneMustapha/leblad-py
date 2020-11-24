import json

class Api:
    data = json.load(open("../../data/WilayaList.json", encoding="utf-8"))
    
    def getWilayaList(self):
        wilaya_list = [ d['name'] for d in self.data ]
        return  wilaya_list
        
    def getWilayaByCode(self,  wilaya_code):
        def search(_data, wilaya_code):
            return list(filter(lambda i :  i['mattricule'] == wilaya_code, _data))
        
        return search(self.data, wilaya_code)[0]
    
    def getWilayaByZipCode(self, zip_code):
        def search(_data, wilaya_code):
            return list(filter(lambda i :  int(wilaya_code) in   i['postalCodes'], _data))
    
        return search(self.data, zip_code)[0]

a  =  Api()

