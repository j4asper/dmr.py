from datetime import datetime

from typing import Optional

from .propulsion import Propulsion

from .insurance import Insurance

from pydantic import (
    BaseModel,
    create_model,
)


class Vehicle(BaseModel):
    make: str
    model: str
    variant: str
    type: str  # ENUM ??
    color: Optional[str]
    total_weight: int
    vin: str
    last_update: datetime
    registration_number: str
    first_registration: datetime
    use: str
    model_year: Optional[int]
    vehicle_weight: Optional[int]
    propulsion: Propulsion
    tow_bar: bool
    fuel_consumption: Optional[float]
    cylinders: Optional[int]
    plugin_hybrid: bool
    electricity_consumption: Optional[float]
    electric_range: Optional[float]
    battery_capacity: Optional[float]
    body_type: Optional[str]  # ENUM ???
    vehicle_id: int
    doors: Optional[int]
    particle_filter: Optional[bool]
    insurance: create_model("Insurance", __base__=Insurance)
