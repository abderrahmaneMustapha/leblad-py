


def GetBaladiyatsFromWilayaObject(dairats, daira): 
    for daira_element in dairats:
        if daira.lower()== daira_element["name"].lower():
            return  daira_element["baladyiats"], True
    
    return None, False
    