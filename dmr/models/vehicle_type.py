from enum import Enum


class VehicleType(str, Enum):
    car = "Personbil"
    van = "Varebil"
    truck = "Lastbil"
    tractor = "Traktor"
    motorcycle = "Motorcykel"
    moped = "Lille knallert"
    large_moped = "Stor knallert"
    bus = "Stor personbil"  # Busses are registered as "Stor personbil"
