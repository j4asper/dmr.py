# dmr.py  
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dmr.py?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/dmr.py?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dmr.py?style=for-the-badge)  
You will no longer need an exspensive API for danish licens plate lookups with dmr.py, this tool scrapes motorregister.skat.dk directly and returns the data for you to use in your application.  

## Installation:  
Install with pip
```
python -m pip install dmr.py
```  

Install current code from this repo, you will need to have git installed in order to do this.
```
python -m pip install git+https://github.com/j4asper/dmr.py
```


## Example  

synchronously  
```python
from dmr import DMR

licens_plate = "cw87553"

# Get DMR object with data
vehicle = DMR().get_by_plate(licens_plate)

print("The vehicle make is:", vehicle.make)
```

Asynchronously  
```python
from dmr import DMR

licens_plate = "cw87553"

# Get DMR object with data
vehicle = await DMR().get_by_plate_async(licens_plate)

print("The vehicle make is:", vehicle.make)
```

**All attributes to the DMR() object [can be viewed in the Wiki](https://github.com/j4asper/dmr.py/wiki/DMR-Attributes 'Click here to go to the Wiki')**

## Contributing:
I would be more than happy if those who know how to make pull requests, contribute with code!  

## ToDo
- [ ] Add from_json and to_json functions.  
- [x] Add documentation with all possible values.  
- [ ] Scrape more parts of the DMR site to get even more data. 
- [ ] Add wider tests with different types of cars or bikes.  

## Issue we can't do anything about.  
If you have used this tool, you might notice that it is slow AF. That is probably due to our government using multiple 80-100 GB XML files as the databse for all vehicles in Denmark. It roughly takes about 3 seconds to do a lookup on the DMR site.
