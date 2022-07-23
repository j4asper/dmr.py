from .utils import scrape_async, scrape

class DMR:
    def __init__(self, make=None, model=None, variant=None, type=None, color=None, total_weight=None, vin=None, last_update=None, licens_plate=None, first_registration=None, use=None, model_year=None, vehicle_weight=None, propulsion=None, tow_bar=None, fuel_consumption=None, cylinders=None, plugin_hybrid=None, electricity_consumption=None, electric_range=None, battery_capacity=None, body_type=None, raw_data=None):
        self.make = make
        self.model = model
        self.variant = variant
        self.type = type
        self.color = color
        self.colour = color
        self.total_weight = total_weight
        self.vin = vin
        self.last_update = last_update
        self.licens_plate = licens_plate
        self.first_registration = first_registration
        self.use = use
        self.model_year = model_year
        self.vehicle_weight = vehicle_weight
        self.propulsion = propulsion
        self.tow_bar = tow_bar
        self.fuel_consumption = fuel_consumption
        self.cylinders = cylinders
        self.plugin_hybrid = plugin_hybrid
        self.electricity_consumption = electricity_consumption
        self.electric_range = electric_range
        self.battery_capacity = battery_capacity
        self.body_type = body_type
        
        self.raw_data = raw_data

    def __from_dict(self, data):
        # MAKE DATETIME OBJECT last_update and first_registration
        return DMR(
            make=data["make"],
            model=data["model"],
            variant=data["variant"],
            type=data["type"],
            color=data["color"],
            total_weight=data["total_weight"],
            vin=data["vin"],
            last_update=data["last_update"],
            licens_plate=data["registration_number"],
            first_registration=data["first_registration"],
            use=data["use"],
            model_year=data["model_year"],
            vehicle_weight=data["vehicle_weight"],
            propulsion=data["propulsion"],
            tow_bar=data["tow_bar"],
            fuel_consumption=data["fuel_consumption"],
            cylinders=data["cylinders"],
            plugin_hybrid=data["plugin_hybrid"],
            electricity_consumption=data["electricity_consumption"],
            electric_range=data["electric_range"],
            battery_capacity=data["battery_capacity"],
            body_type=data["body_type"],
            raw_data=data
        )

    def get_by_plate(self, license_plate:str):
        """Get data from DMR by license plate.

        Args:
            license_plate (str): The licens plate that should be searched for
        """
        if len(license_plate) > 7 or len(license_plate) < 2:
            raise TypeError("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")

        data = scrape(license_plate)
        if data == None:
            return None
        else:
            dmr_obj = self.__from_dict(data)
            return dmr_obj

    async def get_by_plate_async(self, license_plate:str):
        """Get data from DMR asynchronously by license plate.

        Args:
            license_plate (str): The licens plate that should be searched for
        """
        if len(license_plate) > 7 or len(license_plate) < 2:
            raise TypeError("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")
        
        data = await scrape_async(license_plate)
        if data == None:
            return None
        else:
            dmr_obj = self.__from_dict(data)
            return dmr_obj