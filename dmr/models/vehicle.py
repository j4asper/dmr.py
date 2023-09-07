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
        type:
        color:
        total_weight:
        vin:
        last_update:
        registration_number:
        first_registration:
        use:
        model_year:
        vehicle_weight:
        propulsion:
        tow_bar:
        fuel_consumption:
        cylinders:
        plugin_hybrid:
        electricity_consumption:
        electric_range:
        battery_capacity:
        body_type:
        vehicle_id:
        doors:
        particle_filter:
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
    body_type: Optional[BodyType]  # ENUM ???
    vehicle_id: int
    doors: Optional[int]
    particle_filter: Optional[bool]
    insurance: create_model("Insurance", __base__=Insurance)
