# Leblad py

the python version of leblad library, provide a list of Algerian administrative areas with many useful APIs
based on [dzcode-io/leblad](https://github.com/dzcode-io/leblad)

# Meta 

**Coverage** 

[![codecov](https://codecov.io/gh/abderrahmaneMustapha/leblad-py/branch/main/graph/badge.svg?token=G2LWO5YXHB)](https://codecov.io/gh/abderrahmaneMustapha/leblad-py)
## Getting started

### Usage

### Installation

```
pip install leblad
```

## API

### import

```python
import leblad

api   =   leblad.Api()
```

### getWilayaList

Returns a list of algeria provinces or wilayas

#### Arguments

-   return : Array of Wilaya Object attributes to keep

#### Examples

```python
allWilayasDetails = api.getWilayaList()
```

### getWilayaByZipCode

Returns a wilaya that includes the given zipCode

#### Arguments

-   `zip_code` number (required) A zip code
    return : Array of Wilaya Object attributes to keep
    **Examples**

```python
wilaya = api.getWilayaByZipCode(zip_code)
```

### getWilayaByCode

Returns a wilaya that includes the given wilaya code (mattricule).

#### Arguments

-   `wilaya_code` number (**required**) A zip code
    return : Array of Wilaya Object attributes to keep

**Examples**

```python
wilaya = api.getWilayaByCode(14)
print(wilaya) # will print the wilaya object ({name: "Tiaret"...})
```

### getAdjacentWilayas

Takes a wilaya code (matricule) and returns a list of adjacent wilayas codes

**Arguments**

-   `wilaya_code` (**required**) the Wilaya's "matricule"

**Examples**

```python
adjacent_wilayas = api.getAdjacentWilaya(31)
print(adjacent_wilayas) # will print [46, 22, 29, 27]
```

### getZipCodesForWilaya

Takes a wilaya code (matricule) and returns a list of Respective Zip-Codes for that wilaya

**Arguments**

-   `wilaya_code` (**required**) the Wilaya's "matricule"

**Examples**

```python
wilayas_zipcodes = api.getZipCodesForWilaya(31)
print(wilayas_zipcodes) #returns list of zip codes for wilaya 31
```

#### getWilayasByPhoneCode

Takes a phone code and returns the matching wilaya.

**Arguments**

-   `phone_code` (**required**) the Wilaya's "phoneCode"

**Examples**

```python
wilaya = api.getWilayasByPhoneCode(34)
print(wilaya) # will the wilaya object ({name: "Béjaïa"...})
```

### getWilayaByDairaName

Takes a daira name and returns the matching wilaya.

**Arguments**

-   `dairaName: string` (**required**) the Wilaya's "dairaName"

**Examples**

```python
wilaya = api.getWilayaByDairaName("OUED RHIOU")
print(wilaya) #will print the wilaya object ({name: "Relizane"...})
```

#### getBaladyiatsForDaira

Takes a daira code and returns the matching baladyiats.

**Arguments**

-   `daira_code: int` (**required**) the Wilaya's "dairaName"

**Examples**

```python
baladiyats = api.getBaladyiatsForDaira(1401)
print(baladiyats) # will return baladyiats for daira of "Tiaret"
```

### getDairatsForWilaya

Takes a wilaya code (matricule) ans returns list of all dairats of that wilaya.

**Arguments**

-   `wilaya_code: number` (**required**) the Wilaya's "matricule"

**Examples**

```python
wilaya_dairats = api.getDairatsForWilaya(3)
print(wilaya_dairats) #returns list of dairats for wilaya 3
```

#### getPhoneCodesForWilaya

Takes a wilaya code (matricule) and returns a list of phone codes for given wilaya

**Arguments**

-   `wilaya_code: number` (**required**) the Wilaya's "matricule"

**Examples**

```python
phones  = api.getPhoneCodesForWilaya(22)
print(phones) #returns list of phone codes for wilaya 22
```

#### getFirstPhoneCodeForWilaya

Takes a wilaya code (matricule) and returns the first phone code from a list of phone codes for given wilaya

**Arguments**

-   `wilayaCode: number` (**required**) the Wilaya's "matricule"

**Examples**

```python
first_phonecode = api.getFirstPhoneCodeForWilaya(16)
print(first_phonecode) #returns first phone code for wilaya 16
```

### getBaladyiatsForWilaya

Takes a wilaya code (mattricule) and returns array of Baladiyates of wilaya.

**Arguments**

-   `wilaya_code: number` (**required**) the Wilaya's "matricule"

**Examples**

```python
wilaya_bladiyats = api.getBaladyiatsForWilaya(31)
print(wilaya_bladiyats) # will print the baladyiats list ([{ code: 3125, name: 'AIN KERMA'..},{ code: 3105,name: 'ES SENIA',}])
```

### getWilayaByBaladyiaName

Takes a Baladyia name and returns wilaya in which baladyia is located.

**Arguments**

-   `baladya: number` (**required**) the Baladyia name

**Examples**

```python
wilaya = api.getWilayaByBaladyiaName('ES SENIA')
print(wilaya) # will print the wilaya object ({name: "Oran"...})
```

### getDairaByBaladyiaName

Takes a Baladyia name and returns daira in which baladyia is located.

**Arguments**

-   `baladyia_name: string` (**required**) the Baladyia name

**Examples**

```python
daira =api.getDairaByBaladyiaName('ES SENIA')
print(daira) #will print the daira object ({name: "ES SENIA"...})
```

### getFullAdjacentWilaya

Takes a wilaya code  and returns a list of adjacent wilaya objects

**Arguments**

-   `wilaya_code: integer` (**required**) the wilaya code (matricule)

**Examples**

```python
adjacent_wilaya_obj =api.getFullAdjacentWilaya('14')
print(adjacent_wilaya_obj) #will print a list of objects of adjacent wilaya
```
### getAdjacentWilaya

Takes a wilaya code  and returns a list of adjacent wilayas

**Arguments**

-   `wilaya_code: integer` (**required**) the wilaya code (matricule)

**Examples**

```python
adjacent_wilaya_obj =api.getAdjacentWilaya('14')
print(adjacent_wilaya_obj) #will print a list of objects of adjacent wilaya
```
## Testing

Simply run

```python
python -m unittest tests/test_index.py
```

## License

Copyright (c) 2020 Licensed under the MIT license.
