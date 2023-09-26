[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dmr.py?style=for-the-badge)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/dmr.py?style=for-the-badge)](https://pypi.org/project/dmr.py/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/dmr.py?style=for-the-badge)](https://pypi.org/project/dmr.py/)  
[![GitHub](https://img.shields.io/github/license/j4asper/dmr.py?style=for-the-badge)](https://github.com/j4asper/dmr.py/blob/main/LICENSE)
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/jazper 'Click here to donate')  

# dmr.py

You will no longer need an exspensive API for danish license plate lookups with dmr.py, this tool scrapes the [danish vehicle registry](https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej 'motorregister.skat.dk') directly and returns the data for you to use in your application. Be aware, that because of skat.dk's very slow database lookups, it could take about 3-4 seconds before getting a response.  

## Table of Contents

- [Installation](#installation)
  - [From Pip](#from-pip)
  - [From Source](#from-source)
- [Examples](#examples)
  - [Synchronous Get](#synchronous-get)
  - [Asynchronous Get](#asynchronous-get)
  - [Validating License Plates](#validating-license-plates)
  - [Models to dict/json](#models-to-dictjson)
  - [Unit Conversion](#unit-conversion)
- [Contributing](#contributing)
- [Issue we can't do anything about](#issue-we-cant-do-anything-about)
- [License Plates for testing](#license-plates-for-testing)

## Installation

### From Pip

```console
python -m pip install dmr.py
```  

### From Source

Install current code from this repo, you will need to have [git](https://git-scm.com/downloads) installed in order to do this. The code in the repo might not match the current release, if you experience errors you should switch back the the latest release.

```console
python -m pip install git+https://github.com/j4asper/dmr.py
```

## Examples

The library is very easy to use, these two examples might be the only methods you need to know.

### Synchronous Get

Get a [Vehicle object](/dmr/models/vehicle.py) synchronously.

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

### Asynchronous Get

Get a [Vehicle object](/dmr/models/vehicle.py) asynchronously.

```python
from dmr import DMR

license_plate = "cw87553"

# Get Vehicle object with data
vehicle = await DMR.get_by_plate_async(license_plate)

print("The vehicle make is:", vehicle.make)
# The vehicle make is: Suzuki
```

### Validating License Plates

This is the easiest way to check if a license plate is in a valid format. This will only check if the format is valid, not if the license plate actually exists. This check is also used when using the get_by_plate() method.

```python
from dmr import DMR

is_valid = DMR.validate_license_plate("cw87553")
# True

is_valid = DMR.validate_license_plate("Very Cool")
# False

is_valid = DMR.validate_license_plate("GGGGGGG")
# True
```

### Models to dict/json

The model classes are [Pydantic BaseModels](https://docs.pydantic.dev/latest/api/base_model/) or Enums. These are easily converted into a dict or a json string. I have listed 3 main methods of doing it.

```python
from dmr import DMR

# Get Vehicle object
vehicle = DMR.get_by_plate("cw87553")


# If you want your model as a JSON string, this is the method to use. This is the equivalent of using json.dumps() on a dictionary.
vehicle.model_dump_json()

# Preferred method to use if you want sub models to be made into dicts as well
vehicle.model_dump()

# This is not recommeded, because the underlying Insurance object isn't parsed as a dictionary.
dict(vehicle)
```

### Unit Conversion

The default units used in this library is metric. A [Converter](/dmr/converter.py) class has been implemented, to make it easier to convert units to imperial and the other way around.

```python
from dmr import Converter

range_in_km = 100

range_in_miles = Converter.km_to_miles(range_in_km)

print("Range in miles:", range_in_miles)
# Range in miles: 62.14
```

## Contributing

I would be more than happy if those who know how to make pull requests, contribute with code! Sometimes XPaths may not match with the ones on the [danish vehicle registry](https://motorregister.skat.dk/dmr-kerne/koeretoejdetaljer/visKoeretoej 'motorregister.skat.dk'), if that's the case, then you can either make a pull request with XPath fixes or make an issue saying that the XPaths are wrong, then I will fix it. XPaths are kept in [this file](https://github.com/j4asper/dmr.py/blob/main/dmr/utils/xpaths.py).  

## ToDo

- [x] Add documentation with all possible values.  
- [ ] Scrape more parts of the DMR site to get even more data.  
- [x] Add more broad tests with different types of cars or bikes.  

## Issue we can't do anything about

If you have used this tool, you might notice that it's very slow. That is probably due to our government using multiple 80-100 GB XML files as the databse for all vehicles in Denmark. It roughly takes about 3 seconds to do a lookup on the DMR site. Caching is __highly__ recommended!  

## License Plates for testing

This is a collectoin of license plates that you can use for testing.

You can find the list [here](https://github.com/j4asper/dmr.py/blob/main/license_plates.txt). Most of the license plates in this file should be valid.
