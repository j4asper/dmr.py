

ONE_MILE_IN_KM = 0.6213711922
ONE_KM_IN_MILES = 1.609344

ONE_POUND_IN_KG = 2.204623
ONE_KG_IN_POUNDS = 0.4535923


class Converter:

    @classmethod
    def km_to_miles(cls, km: int, decimals: int = 2):
        """Convert Kilometers to Miles"""
        miles = km * ONE_MILE_IN_KM
        return round(miles, decimals)

    @classmethod
    def miles_to_km(cls, miles: int, decimals: int = 2):
        """Convert Miles to Kilometers"""
        km = miles * ONE_KM_IN_MILES
        return round(km, decimals)

    @classmethod
    def kg_to_lb(cls, kg: int, decimals: int = 2):
        """Convert Kilograms to Pounds"""
        lb = kg * ONE_POUND_IN_KG
        return round(lb, decimals)

    @classmethod
    def lb_to_kg(cls, lb: int, decimals: int = 2):
        """Convert Pounds to Kilograms"""
        kg = lb * ONE_KG_IN_POUNDS
        return round(kg, decimals)
