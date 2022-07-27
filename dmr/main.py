from .utils import scrape_async, scrape

class DMR:
    def __init__(self, make=None, model=None, variant=None, type=None, color=None, total_weight=None, vin=None, last_update=None, registration_number=None, first_registration=None, use=None, model_year=None, vehicle_weight=None, propulsion=None, tow_bar=None, fuel_consumption=None, cylinders=None, plugin_hybrid=None, electricity_consumption=None, electric_range=None, battery_capacity=None, body_type=None, raw_data=None, vehicle_id=None, doors=None, particle_filter=None):
        self.make = make
        self.model = model
        self.variant = variant
        self.type = type
        self.color = color
        self.colour = color
        self.total_weight = total_weight
        self.vin = vin
        self.last_update = last_update
        self.registration_number = registration_number
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
        self.vehicle_id = vehicle_id
        self.doors = doors
        self.particle_filter = particle_filter

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
            registration_number=data["registration_number"],
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
            vehicle_id = data["vehicle_id"],
            doors = data["doors"],
            particle_filter = data["particle_filter"],
            raw_data=data,
        )

    def validate_license_plate(self, license_plate:str):
        """Checks if the given string can be a license plate, this check is prior to the webscraping.

        Args:
            license_plate (str): The license plate to check

        Returns:
            bool: Returns True if the string could be a license plate, or False if not.
        """
        return len(license_plate) <= 7 and len(license_plate) >= 2 and license_plate.isalnum()

    def to_dict(self):
        """Get JSON version of the object with object attributes as keys, and corresponding values.

        Returns:
            Dict: Returns the object in a Dictionary/JSON format.
        """
        return self.raw_data

    def get_by_plate(self, license_plate:str):
        """Get data from DMR by license plate.

        Args:
            license_plate (str): The licens plate to look up.

        Raises:
            TypeError: Invalid licens plate was given

        Returns:
            DMR: DMR object is returned, check https://github.com/j4asper/dmr.py/wiki for more information.
        """
        if not self.validate_license_plate(license_plate):
            raise TypeError("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")

        data = scrape(license_plate=license_plate)
        return None if data == None else self.__from_dict(data)

    async def get_by_plate_async(self, license_plate:str):
        """Get data from DMR asynchronously by license plate.

        Args:
            license_plate (str): The licens plate to look up.

        Raises:
            TypeError: Invalid licens plate was given

        Returns:
            DMR: DMR object is returned, check https://github.com/j4asper/dmr.py/wiki for more information.
        """
        if not self.validate_license_plate(license_plate):
            raise TypeError("Invalid license plate. Licens plate length should be between 2 and 7 letters and/or digits.")

        data = await scrape_async(license_plate=license_plate)
        return None if data == None else self.__from_dict(data)