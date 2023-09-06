from enum import Enum


class Propulsion(str, Enum):
    diesel = "Diesel"
    benzin = "Benzin"
    electric = "El"
    hydrogen = "Brint"
