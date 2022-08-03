from __future__ import annotations
from .utils import scrape_async, scrape, errors
from pydantic import BaseModel
from typing import Optional
import datetime

class DMR:
    def __init__(self, registration_number:str=None):
        self._registration_number = registration_number

    def __from_dict(self, data):
        self._make = data["make"]
        self._model=data["model"]
        self._variant=data["variant"]
        self._type=data["type"]
        self._color=data["color"]
        self._total_weight=data["total_weight"]
        self._vin=data["vin"]
        self._last_update=data["last_update"]
        self._registration_number=data["registration_number"]
        self._first_registration=data["first_registration"]
        self._use=data["use"]
        self._model_year=data["model_year"]
        self._vehicle_weight=data["vehicle_weight"]
        self._propulsion=data["propulsion"]
        self._tow_bar=data["tow_bar"]
        self._fuel_consumption=data["fuel_consumption"]
        self._cylinders=data["cylinders"]
        self._plugin_hybrid=data["plugin_hybrid"]
        self._electricity_consumption=data["electricity_consumption"]
        self._electric_range=data["electric_range"]
        self._battery_capacity=data["battery_capacity"]
        self._body_type=data["body_type"]
        self._vehicle_id = data["vehicle_id"]
        self._doors = data["doors"]
        self._particle_filter = data["particle_filter"]
        self._raw_data=data
        self._insurance = Insurance(**data["insurance"])
        return self
        
    def validate_license_plate(self, license_plate:str):
        """Checks if the given string can be a license plate, this check is prior to the webscraping.

        Args:
            license_plate (str): The license plate to check

        Returns:
            bool: Returns True if the string could be a license plate, or False if not.
        """
        return len(license_plate) <= 7 and len(license_plate) >= 2 and license_plate.isalnum()

    def to_dict(self):
        """Get JSON version of the object with object attributes as keys, and corresponding values.

        Returns:
            Dict: Returns the object in a Dictionary/JSON format.
        """
        return self.raw_data

    def get_by_plate(self, license_plate:str=None):
        """Get data from DMR by license plate.

        Args:
            license_plate (str): The licens plate to look up. Not required if license plate was passed into the DMR object.

        Raises:
            InvalidLicensePlate: Invalid licens plate was given

        Returns:
            DMR: DMR object is returned, check https://github.com/j4asper/dmr.py/wiki for more information.
        """
        if self._registration_number is None and license_plate is None:
            raise ValueError("No registration number/license plate was passed into the DMR object or the get_by_plate() function.")
        
        license_plate = self._registration_number if license_plate is None else license_plate
        
        if not self.validate_license_plate(license_plate):
            raise errors.InvalidLicensePlate("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")

        data = scrape(license_plate=license_plate)
        return None if data is None else self.__from_dict(data)

    async def get_by_plate_async(self, license_plate:str=None):
        """Get data from DMR asynchronously by license plate.

        Args:
            license_plate (str): The licens plate to look up.

        Raises:
            InvalidLicensePlate: Invalid licens plate was given

        Returns:
            DMR: DMR object is returned, check https://github.com/j4asper/dmr.py/wiki for more information.
        """
        if self._registration_number is None and license_plate is None:
            raise ValueError("No registration number/license plate was passed into the DMR object or the get_by_plate() function.")
        
        license_plate = self._registration_number if license_plate is None else license_plate
        
        if not self.validate_license_plate(license_plate):
            raise errors.InvalidLicensePlate("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")

        data = await scrape_async(license_plate=license_plate)
        return None if data is None else self.__from_dict(data)
    

    @property
    def make(self) -> str:
        """The make/manufacturer of the vehicle"""
        return self._make

    @property
    def model(self) -> str:
        """The vehicle model, if the vehicle were to be a Suzuki Swift, then the model would be "Swift\""""
        return self._model

    @property
    def variant(self) -> str:
        """This is the variant of the model, a VW Golf GTI, would have the GTI variation of the Golf model."""
        return self._variant

    @property
    def type(self) -> str:
        """The type of vehicle, this could be "Personbil"."""
        return self._type

    @property
    def color(self) -> Optional[str]:
        """The color of the vehicle, typically None."""
        return self._color

    @property
    def total_weight(self) -> int:
        """The maximum weight the vehicle can be when fully loaded, value is in KG."""
        return self._total_weight

    @property
    def vin(self) -> str:
        """The vehicles identification number (VIN)"""
        return self._vin

    @property
    def last_update(self) -> datetime.datetime:
        """The last vehicle update, this could be the latest re-registration."""
        return self._last_update

    @property
    def registration_number(self) -> str:
        """The vehicles license plate."""
        return self._registration_number

    @property
    def first_registration(self) -> datetime.datetime:
        """The date where the vehicle was first registered."""
        return self._first_registration

    @property
    def use(self) -> str:
        """The usage of the vehicle. This could be "Godstransport privat/erhverv" if it's a work vehicle or "Privat personkørsel" if it's a personal vehicle."""
        return self._use

    @property
    def model_year(self) -> Optional[int]:
        """The model year of the vehicle."""
        return self._model_year

    @property
    def vehicle_weight(self) -> Optional[int]:
        """The weight of the vehicle. The value returned is in KG."""
        return self._vehicle_weight

    @property
    def propulsion(self) -> str:
        """The type "Fuel" needed to use the vehicle, this could return "Benzin", "Brint", "Diesel" or "El"."""
        return self._propulsion

    @property
    def tow_bar(self) -> bool:
        """If the vehicle has a tow bar."""
        return self._tow_bar

    @property
    def fuel_consumption(self) -> Optional[float]:
        """The fuel consumption of the vehicle, the value can be km/L if the vehicle runs on Benzin or Diesel. If the vehicle is a Plug-In hybrid, then this and "electric_consumption" will return a value."""
        return self._fuel_consumption

    @property
    def cylinders(self) -> Optional[int]:
        """The amount of cylinders the vehicle has. A return value of None doesn't necessarily mean that the vehicle has no cylinders."""
        return self._cylinders

    @property
    def plugin_hybrid(self) -> Optional[bool]:
        """If the vehicle is a Plug-In hybrid."""
        return self._plugin_hybrid

    @property
    def electricity_consumption(self) -> Optional[float]:
        """The electric consumption of the vehicle, the value can be Wh/km. If the vehicle is a Plug-In hybrid, then this and "fuel_consumption" will return a value."""
        return self._electricity_consumption

    @property
    def electric_range(self) -> Optional[float]:
        """The electric range of the vehicle, value is in km."""
        return self._electric_range

    @property
    def battery_capacity(self) -> Optional[float]:
        """The battery capacity of the vehicle, value is in kWh."""
        return self._battery_capacity

    @property
    def body_type(self) -> Optional[str]:
        """The body type of the vehicle, it can be fx "Stationcar"."""
        return self._body_type

    @property
    def vehicle_id(self) -> int:
        """The vehicle ID in the DMR system, it is probably a randomly generated ID by DMR."""
        return self._vehicle_id

    @property
    def doors(self) -> Optional[int]:
        """The amount of doors the vehicle has."""
        return self._doors

    @property
    def particle_filter(self) -> Optional[bool]:
        """If the vehicle has a particle filter."""
        return self._particle_filter

    @property
    def raw_data(self) -> Optional[dict]:
        """A dictionary version of the DMR object."""
        return self._raw_data

    @property
    def insurance(self) -> Insurance:
        """An insurance object with insurance specifications."""
        return self._insurance


class Insurance(BaseModel):
    """
    The Insurance object holds the insurance information about the vehicle.

    Possible attributes:

        Insurance.company (str): The insurance provider.

        Insurance.is_active (bool): Whether or not the insurance is active.

        Insurance.number (str): The insurance number, typically returns None.

        Insurance.created (datetime): The date when the insurance was created.
    """
    company:str
    is_active:bool
    number:Optional[int]
    created:datetime.datetime
