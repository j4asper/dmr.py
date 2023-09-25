[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dmr.py?style=for-the-badge)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/dmr.py?style=for-the-badge)](https://pypi.org/project/dmr.py/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dmr.py?style=for-the-badge)](https://pypi.org/project/dmr.py/)  
[![GitHub](https://img.shields.io/github/license/j4asper/dmr.py?style=for-the-badge)](https://github.com/j4asper/dmr.py/blob/main/LICENSE)
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/jazper 'Click here to donate')  

# dmr.py

You will no longer need an exspensive API for danish license plate lookups with dmr.py, this tool scrapes the [danish vehicle registry](https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej 'motorregister.skat.dk') directly and returns the data for you to use in your application. Be aware, that because of skat.dk's very slow database lookups, it could take about 3-4 seconds before getting a response.  

## Installation

Install with pip

```console
python -m pip install dmr.py
```  

If you want to install the additional speedup packages, you can use the command below. These speedup packages is only for the async part of this library. If you are only using the synchronous part, then this is unnecessary.

```console
python -m pip install dmr.py[speed]
```

Install current code from this repo, you will need to have git installed in order to do this. The code in the repo might not match the current release, if you experience errors you should switch back the the latest release.

```console
python -m pip install git+https://github.com/j4asper/dmr.py
```

## Example

The library is very easy to use, these two examples might be the only methods you need to know.

**Synchronously**

```python
from dmr import DMR
# Import models directly if needed:
from dmr.models import *

license_plate = "cw87553"

# Get Vehicle object with data
vehicle: Vehicle = DMR.get_by_plate(license_plate)

print("The vehicle make is:", vehicle.make)
# The vehicle make is: Suzuki
```

---

**Asynchronously**

```python
from dmr import DMR

license_plate = "cw87553"

# Get Vehicle object with data
vehicle = await DMR.get_by_plate_async(license_plate)

print("The vehicle make is:", vehicle.make)
# The vehicle make is: Suzuki
```

**Models to dict/json**

The model classes are [Pydantic BaseModels](https://docs.pydantic.dev/latest/api/base_model/) or Enums.

```python
from dmr import DMR

license_plate = "cw87553"

# Get Vehicle object with data
vehicle = await DMR.get_by_plate_async(license_plate)

print(vehicle.model_dump()) # .model_dump() returns a dict
# {'make': 'Suzuki', 'model': 'Swift', 'variant': '1,5', ........}
```

## Contributing

I would be more than happy if those who know how to make pull requests, contribute with code! Sometimes XPaths may not match with the ones on the [danish vehicle register](https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej 'motorregister.skat.dk'), if that's the case, then you can either make a pull request with XPath fixes or make an issue saying that the XPaths are wrong, then I will fix it. XPaths are kept in [this file](https://github.com/j4asper/dmr.py/blob/main/dmr/utils/xpaths.py).  

## ToDo

- [x] Add documentation with all possible values.  
- [ ] Scrape more parts of the DMR site to get even more data.  
- [x] Add more broad tests with different types of cars or bikes.  

## Issue we can't do anything about

If you have used this tool, you might notice that it's very slow. That is probably due to our government using multiple 80-100 GB XML files as the databse for all vehicles in Denmark. It roughly takes about 3 seconds to do a lookup on the DMR site. Caching is __highly__ recommended!  

## License Plates for testing

You can use all the license plates listed in [**This file**](https://github.com/j4asper/dmr.py/blob/main/license_plates.txt 'Click here') for testing. If a license plate turns out to be invalid, please remove it and make a PR, or create an issue stating this.
