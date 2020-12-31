# Leblad py
the python version of leblad library,  provide a list of Algerian administrative areas with many useful APIs 
based on  [dzcode-io/leblad](https://github.com/dzcode-io/leblad)

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

Returns a list of  algeria provinces or wilayas
#### Arguments 

- return  :  Array of Wilaya Object attributes to keep

#### Examples

```python
allWilayasDetails = api.getWilayaList()
```

### getWilayaByZipCode

Returns a wilaya that includes the given zipCode
#### Arguments

- `zip_code` number (required) A zip code
return :  Array of Wilaya Object attributes to keep
**Examples**

```python
wilaya = api.getWilayaByZipCode(zip_code)
```

### getWilayaByCode

Returns a wilaya that includes the given wilaya code (mattricule).

#### Arguments

-  `wilaya_code` number (**required**) A zip code
return :  Array of Wilaya Object attributes to keep

**Examples**

```python
wilaya = api.getWilayaByCode(14)
print(wilaya) # will print the wilaya object ({name: "Tiaret"...})
```

### getAdjacentWilayas

Takes a wilaya code (matricule) and returns a list of adjacent wilayas codes

**Arguments**

- `wilaya_code` (**required**) the Wilaya's "matricule"

**Examples**

```python
adjacent_wilayas = api.getAdjacentWilayas(31)
print(adjacent_wilayas) # will print [46, 22, 29, 27]
```

### getZipCodesForWilaya

Takes a wilaya code (matricule) and returns a list of Respective Zip-Codes for that wilaya

**Arguments**

- `wilaya_code` (**required**) the Wilaya's "matricule"

**Examples**

```python
wilayas_zipcodes = api.getAdjacentWilayas(31)
print(wilayas_zipcodes) #returns list of zip codes for wilaya 31
```

#### getWilayaByPhoneCode

Takes a phone code and returns the matching wilaya.

**Arguments**

- `phone_code` (**required**) the Wilaya's "phoneCode"

**Examples**

```python
wilaya = api.getWilayaByPhoneCode(34)); 
print(wilaya) # will the wilaya object ({name: "Béjaïa"...})
```

#### Testing
Install unittest 

Simply run

```python
python -m unittest tests/test_index.py
```

## License

Copyright (c) 2020  Licensed under the MIT license.
