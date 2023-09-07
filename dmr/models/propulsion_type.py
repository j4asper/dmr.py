from enum import Enum


class PropulsionType(str, Enum):
    """Vehicle propulsion type, the kind of fuel the car uses"""
    diesel = "Diesel"
    benzin = "Benzin"
    electric = "El"
    hydrogen = "Brint"
    f_gas = "F-Gas"
    petroleum = "Petroleum"
    n_gas = "N-Gas"
    methanol = "Metanol"
    ethanol = "Ætanol"
