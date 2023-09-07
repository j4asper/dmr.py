from enum import Enum


class BodyType(str, Enum):
    """Vehicle body types"""
    cabriolet = "Cabriolet"
    coupe = "Coupe"
    hatchback = "Hatchback"
    mpw = "MPV"
    sedan = "Sedan"
    stationcar = "Stationcar"
    pickup = "Stationcar-pickup"
