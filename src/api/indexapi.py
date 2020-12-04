#python
import json

#utils
from  utils import *

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
            baladiyats, hasGivenDairaName = getBaladiyatsFromWilayaObject(element["dairats"], daira)
            if hasGivenDairaName:
                return baladiyats

    def getBaladyiatsForWilaya(self, wilaya):
        baladiyats_list = []
        for element in self.data:
            baladiyats, hasGivenDairaName = getBaladiyatsFromWilayaObject(element["dairats"], wilaya)
            if hasGivenDairaName:
                baladiyats_list.extend(baladiyats)

        return baladiyats_list
    
    def getDairatsForWilaya(self, wilaya_code):
        wilaya = self.getWilayaByCode(wilaya_code)
        dairats  = [reduceDict(daira, ["baladyiats"]) for daira  in wilaya['dairats']]
        return dairats

    def getDairaByBaladyiaName(self, baladiya):
        for wilaya in self.data :
             for daira in wilaya['dairats'] :
                try : 

                    for _baladiya in daira['baladyiats']:
                        if  baladiya.lower() in _baladiya['name'].lower():
                            return daira
                except KeyError as e:
                    print("no baladiyats for {}".format(daira['name']))
                    continue


a  =  Api()
a.getDairaByBaladyiaName("SENDJAS")


