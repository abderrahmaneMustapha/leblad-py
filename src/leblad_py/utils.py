

def getBaladiyatsFromWilayaObject(dairats, daira): 
    for daira_element in dairats:
        if daira == daira_element["code"] :
            try :
                return  daira_element["baladyiats"], True
            except KeyError as e:
                print("baldiyats doest not exist for this daira")
    
    return None, False

def reduceDict(_object, exclude_fields):
    for field in exclude_fields : 
        try:
            del _object[str(field)]
        except KeyError as  e:
            print(" this  {} field does not exist  ".format(field))
    return _object