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
Returns a wilaya that includes the given zipCode.

#### Arguments

zipCode: number (required) A zip code
return :  Array of Wilaya Object attributes to keep
## License

Copyright (c) 2020  Licensed under the MIT license.
