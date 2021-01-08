"""
this is the main file of leblad api
"""
import json

#utils
from leblad.utils import getBaladiyatsFromWilayaObject, reduceDict
class Api:
    """
     main class for leblad api
    """
    data = json.load(open("./data/WilayaList.json", encoding="utf-8"))

    def getWilayaList(self):
        """
        this fucntion return all wilayas in the dataset
        """
        wilaya_list = [ wilaya["name"] for wilaya in self.data ]
        return  wilaya_list

    def getWilayaByCode(self,  wilaya_code):
        """
            this fucntion take wilaya  code  as an input (mattricule)
            and return  a wilaya dictionary
        """
        def search(_data, wilaya_code):
            """
            this fucntion take all the wilaya list json dataset, with a wilaya code (mattricule)
            and return a list contain a one element ( wilaya object or dictionary)
            """
            return list(filter(lambda i :  i["mattricule"] == wilaya_code, _data))
        return search(self.data, int(wilaya_code))[0]

    def getWilayaByZipCode(self, zip_code):
        """
            this fucntion take zip code  as an input (postal code)
            and return  a wilaya dictionary
        """
        def search(_data, code):
            """
            this fucntion take all the wilaya list json dataset, with a zip code (postal code)
            and search for this zip code in the wilaya object zip codes array
            and return a list contain a one element ( wilaya object or dictionary)
            """
            return list(filter(lambda i :  int(code) in  i["postalCodes"], _data))
        return search(self.data, zip_code)[0]

    def getBaladyiatsForDaira(self, daira):
        """
        this fucntion take daira name as an input
        and return a list of baldiyats in this daira
        """
        for element in self.data:
            baladiyats, has__daira_name = getBaladiyatsFromWilayaObject(element["dairats"], daira)
            if has__daira_name:
                return baladiyats
        return None

    def getBaladyiatsForWilaya(self, wilaya):
        """
        this function take wilaya code as an input
        and return a list of baladiyats in this wilaya
        """
        baladiyats_list = []
        for element in self.data:
            if element["mattricule"] == wilaya:
                for  dairats in  element["dairats"]:
                    try :
                        for baladiya in dairats["baladyiats"]:
                            baladiyats_list.append(baladiya)
                    except KeyError :
                        pass
        return baladiyats_list

    def getDairatsForWilaya(self, wilaya_code):
        """
        this fucntion take wilaya code (mattricule) as an input
        and return a list of dairats objects in this wilaya
        """
        wilaya = self.getWilayaByCode(wilaya_code)
        dairats  = [reduceDict(daira, ["baladyiats"]) for daira  in wilaya["dairats"]]
        return dairats

    def getDairaByBaladyiaName(self, baladiya):
        """
        this function take the baladiya name as an input
        and return a daira object
        """
        for wilaya in self.data :
            for daira in wilaya["dairats"] :
                try :
                    for _baladiya in daira["baladyiats"]:
                        if  baladiya.lower() in _baladiya["name"].lower():
                            return daira

                except KeyError :
                    pass
        return None

    def getFirstPhoneCodeForWilaya(self, wilaya_code):
        """
        this function take wilaya code (mattricule) as an input
        and return a the first phone code in the wilaya object phone codes list
        """
        phone_code = None

        try:
            phone_code = self.getWilayaByCode(wilaya_code)["phoneCodes"][0]
        except KeyError:
            pass
        except IndexError :
            pass
        return phone_code

    def getPhoneCodesForWilaya(self, wilaya_code):
        """
        this function take wilaya code as an input (mattricule)
        and return a list of phone in the wilaya object
        """
        phone_codes = None
        try:
            phone_codes = self.getWilayaByCode(wilaya_code)["phoneCodes"]
        except KeyError:
            pass
        except IndexError:
            pass
        return phone_codes

    def getWilayaByBaladyiaName(self, baladiya):
        """
        this function take baladiya name as an input
        and return  a wilaya object
        """
        for wilaya in self.data :

            for daira in wilaya["dairats"] :
                try :
                    for _baladiya in daira["baladyiats"]:
                        if  baladiya.lower() in _baladiya["name"].lower():
                            return wilaya

                except KeyError:
                    pass
        return None

    def getWilayaByDairaName(self,daira):
        """
        this function take daira name as an input
        and return a wilya object
        """
        for wilaya in self.data:
            for _daira in wilaya["dairats"]:
                if daira.lower() in _daira["name"].lower():
                    return  wilaya
        return None

    def getWilayasByPhoneCode(self, phone_code):
        """
        this function take a phone code as an input
        search for this phone code in each wilaya phone codes list
        and return a wilaya object
        """
        return list(filter(lambda i :  int(phone_code) in   i["phoneCodes"], self.data))[0]

    def getZipCodesForWilaya(self, wilaya_code):
        """
        this function take wilaya code
        and return a list of zip codes of this wilaya
        """
        wilaya  =  self.getWilayaByCode(wilaya_code)
        return wilaya["postalCodes"]

    def getAdjacentWilaya(self, wilaya_code):
        """
        this function take a wilaya code (mattricule) as an input
        and return a list of wilaya codes (mattrucles) of adjacent wilaya
        """
        wilaya = self.getWilayaByCode(wilaya_code)
        return wilaya["adjacentWilayas"]

    def getFullAdjacentWilaya(self, wilaya_code):
        """
        this function take a wilaya code (mattricule) as an input
        and return a list of wilaya dicts (object) of adjacent wilaya
        """
        adjacent_wilaya_ids = self.getAdjacentWilaya(wilaya_code)

        full_adjacent_wilaya = [self.getWilayaByCode(wilaya_code)
        for wilaya_code in adjacent_wilaya_ids]

        return  full_adjacent_wilaya
