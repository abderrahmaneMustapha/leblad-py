"""
this file contain helper fucntions that we are using in the main indexapi.py file
"""


def getBaladiyatsFromWilayaObject(dairats, daira):
    """
    this fucntion take an array of wilaya 'dairats' objects and a daira name
    and return the daira baladiyats and if the daira exist in this wilaya
    """
    for daira_element in dairats:
        if daira == daira_element["code"] :
            try :
                return  daira_element["baladyiats"], True
            except KeyError:
                pass
    return None, False

def reduceDict(_object, exclude_fields):
    """
    this function take a dict object and and array of keys  'exclude_fields'
    and return same object without the keys  in the 'exclude_fields' array
    """
    for field in exclude_fields :
        try:
            del _object[str(field)]
        except KeyError :
            pass
    return _object
