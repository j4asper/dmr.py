from enum import Enum


class PropulsionType(str, Enum):
    diesel = "Diesel"
    benzin = "Benzin"
    electric = "El"
    hydrogen = "Brint"
