from enum import Enum


class PropulsionType(str, Enum):
    """Vehicle propulsion type, the kind of fuel the car uses"""
    diesel = "Diesel"
    benzin = "Benzin"
    electric = "El"
    hydrogen = "Brint"
