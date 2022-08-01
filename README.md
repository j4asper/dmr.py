![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dmr.py?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/dmr.py?style=for-the-badge)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/dmr.py?style=for-the-badge)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/j4asper/dmr.py/dmr%20test?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/j4asper/dmr.py?style=for-the-badge)  

# dmr.py  
You will no longer need an exspensive API for danish license plate lookups with dmr.py, this tool scrapes the [danish vehicle registar](https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej 'motorregister.skat.dk') directly and returns the data for you to use in your application. Be aware, that because of skat.dk's very slow database lookups, it could take about 3-4 seconds before getting a response.  

## Installation:  
Install with pip
```console
python -m pip install dmr.py
```  

If you want to install the additional speedup packages, you can use the command below. These speedup packages is only for the async part of this library. If you are only using the synchronous part, then this is unnecessary.
```console
python -m pip install dmr.py[speed]
```


Install current code from this repo, you will need to have git installed in order to do this.
```console
python -m pip install git+https://github.com/j4asper/dmr.py
```


## Example  

Synchronously  
```python
from dmr import DMR

license_plate = "cw87553"

# Get DMR object with data
vehicle = DMR(license_plate).get_by_plate()

print("The vehicle make is:", vehicle.make)
```

Asynchronously  
```python
from dmr import DMR

license_plate = "cw87553"

# Get DMR object with data
vehicle = await DMR(license_plate).get_by_plate_async()

print("The vehicle make is:", vehicle.make)
```

**All attributes to the DMR() object [can be viewed in the Wiki](https://github.com/j4asper/dmr.py/wiki/DMR-Attributes 'Click here to go to the Wiki')**

## Contributing:
I would be more than happy if those who know how to make pull requests, contribute with code!  

## ToDo
- [x] Add from_dict and to_dict functions.  
- [x] Add documentation with all possible values.  
- [ ] Scrape more parts of the DMR site to get even more data. 
- [x] Add more broad tests with different types of cars or bikes.  

## Issue we can't do anything about.  
If you have used this tool, you might notice that it is slow AF. That is probably due to our government using multiple 80-100 GB XML files as the databse for all vehicles in Denmark. It roughly takes about 3 seconds to do a lookup on the DMR site. Caching is __highly__ recommended!
