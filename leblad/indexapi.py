import json

#utils
from leblad.utils import *
import os
class Api:
    data = json.load(open("./data/WilayaList.json", encoding="utf-8"))
    
    def getWilayaList(self):
        wilaya_list = [ wilaya["name"] for wilaya in self.data ]
        return  wilaya_list
        
    def getWilayaByCode(self,  wilaya_code):
        def search(_data, wilaya_code):
            return list(filter(lambda i :  i["mattricule"] == wilaya_code, _data))
        return search(self.data, int(wilaya_code))[0]
    
    def getWilayaByZipCode(self, zip_code):
        def search(_data, code):
            return list(filter(lambda i :  int(code) in  i["postalCodes"], _data))
        return search(self.data, zip_code)[0]

    def getBaladyiatsForDaira(self, daira):
        for element in self.data:
            baladiyats, hasGivenDairaName = getBaladiyatsFromWilayaObject(element["dairats"], daira)
            if hasGivenDairaName:
                return baladiyats


    def getBaladyiatsForWilaya(self, wilaya):
        baladiyats_list = []
        for element in self.data:
            if element["mattricule"] == wilaya:
                 for  dairats in  element["dairats"]:
                    try : 
                        for baladiya in dairats["baladyiats"]:
                            baladiyats_list.append(baladiya)
                    except KeyError as e :
                        print("baldiyats doest not exist for this daira")
        return baladiyats_list
    
    def getDairatsForWilaya(self, wilaya_code):
        wilaya = self.getWilayaByCode(wilaya_code)
        dairats  = [reduceDict(daira, ["baladyiats"]) for daira  in wilaya["dairats"]]
        return dairats

    def getDairaByBaladyiaName(self, baladiya):
        for wilaya in self.data :
             for daira in wilaya["dairats"] :
                try : 
                    for _baladiya in daira["baladyiats"]:
                        if  baladiya.lower() in _baladiya["name"].lower():
                            return daira

                except KeyError as e:
                    print("no baladiyats for {}".format(daira["name"]))
    
    def getFirstPhoneCodeForWilaya(self, wilaya_code):
        phone_code = None
    
        try:
            phone_code = self.getWilayaByCode(wilaya_code)["phoneCodes"][0]
        except KeyError as e:
            print("cant get phone code for  wilaya code {}".format(wilaya_code))
        except IndexError as e:
            print("phone codes array  for wilaya code {} is empty ".format(wilaya_code))
        
        return phone_code

    def getPhoneCodesForWilaya(self, wilaya_code):
        phone_codes = None
        try:
            phone_codes = self.getWilayaByCode(wilaya_code)["phoneCodes"]
        except KeyError as e:
            print("cant get phone code for  wilaya code {}".format(wilaya_code))
        except IndexError as e:
            print("phone codes array  for wilaya code {} is empty ".format(wilaya_code))
        
        return phone_codes

    def getWilayaByBaladyiaName(self, baladiya):
        for wilaya in self.data :

            for daira in wilaya["dairats"] :
                try : 
                    for _baladiya in daira["baladyiats"]:
                        if  baladiya.lower() in _baladiya["name"].lower():
                            return wilaya

                except KeyError as e:
                    print("no baladiyats for {}".format(daira["name"]))
                
    
    def getWilayaByDairaName(self,daira):
        for wilaya in self.data :
            for _daira in wilaya["dairats"]:
                if daira.lower() in _daira["name"].lower():
                    return  wilaya
    
    def getWilayasByPhoneCode(self, phone_code):
       
        return list(filter(lambda i :  int(phone_code) in   i["phoneCodes"], self.data))[0]

    def getZipCodesForWilaya(self, wilaya_code):
        wilaya  =  self.getWilayaByCode(wilaya_code)
        return wilaya["postalCodes"]

    def getAdjacentWilaya(self, wilaya_code):
        wilaya = self.getWilayaByCode(wilaya_code)
        return wilaya["adjacentWilayas"]

    def getFullAdjacentWilaya(self, wilaya_code):
        adjacent_wilaya_ids = self.getAdjacentWilaya(wilaya_code)
        full_info_about_adjacent_wilaya = [self.getWilayaByCode(__wilaya_code) for __wilaya_code in adjacent_wilaya_ids]
        return  full_info_about_adjacent_wilaya
        





