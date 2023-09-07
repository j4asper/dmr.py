from datetime import datetime
from typing import Optional
from .propulsion_type import PropulsionType
from .vehicle_type import VehicleType
from .body_type import BodyType
from .use_type import UseType
from .insurance import Insurance
from pydantic import (
    BaseModel,
    create_model,
)


class Vehicle(BaseModel):
    """This class represents a vehicle returned from DMR.

    Attributes:
        make:                      The make/manufacturer of the vehicle
        model:                     The vehicle model, if the vehicle were to be a Suzuki Swift, then the model would be "Swift\"
        variant:                   This is the variant of the model, a VW Golf GTI, would have the GTI variation of the Golf model
        type:                      The type of vehicle
        color:                     The color of the vehicle, typically None
        total_weight:              The maximum weight the vehicle can be when fully loaded, value is in KG
        vin:                       The vehicles identification number (VIN)
        last_update:               The last vehicle update, this could be the latest re-registration
        registration_number:       The vehicles license plate
        first_registration:        The date where the vehicle was first registered
        use:                       The type of usage the vehicle is being used for
        model_year:                The model year of the vehicle
        vehicle_weight:            The weight of the vehicle. The value returned is in KG
        propulsion:                The type fuel needed to use the vehicle
        tow_bar:                   Whether the vehicle has a tow bar
        fuel_consumption:          The fuel consumption of the vehicle, the value can be km/L if the vehicle runs on Benzin or Diesel
        cylinders:                 The amount of cylinders the vehicle has. A return value of None doesn't necessarily mean that the vehicle has no cylinders
        plugin_hybrid:             Whether the vehicle is a Plug-In hybrid
        electricity_consumption:   The electric consumption of the vehicle, the value can be Wh/km
        electric_range:            The electric range of the vehicle, value is in km
        battery_capacity:          The battery capacity of the vehicle, value is in kWh
        body_type:                 The body type of the vehicle
        vehicle_id:                The vehicle ID in the DMR system
        doors:                     The amount of doors the vehicle has
        particle_filter:           Whether the vehicle has a particle filter
        insurance:                 An insurance object
    """
    make: str
    model: str
    variant: str
    type: VehicleType
    color: Optional[str]
    total_weight: int
    vin: str
    last_update: datetime
    registration_number: str
    first_registration: datetime
    use: UseType
    model_year: Optional[int]
    vehicle_weight: Optional[int]
    propulsion: PropulsionType
    tow_bar: bool
    fuel_consumption: Optional[float]
    cylinders: Optional[int]
    plugin_hybrid: bool
    electricity_consumption: Optional[float]
    electric_range: Optional[float]
    battery_capacity: Optional[float]
    body_type: Optional[BodyType]
    vehicle_id: int
    doors: Optional[int]
    particle_filter: Optional[bool]
    insurance: create_model("Insurance", __base__=Insurance)
