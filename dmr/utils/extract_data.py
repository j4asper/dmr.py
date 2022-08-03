from .xpaths import XPATHS

def get_value_from_xpath(source, xpath_string):
    return source.xpath(xpath_string)[0].text_content()

# Landing page when looking up a licens plate, the page title is "1. Køretøj"
def page_1(source):
    data = dict()
    make, model, variant = get_value_from_xpath(source, XPATHS["page_1"]["make_model_variant"]).split(",", 2)
    # Make make/model/variant names prettier
    data["make"] = make.strip().capitalize()
    data["model"] = model.strip().capitalize()
    data["variant"] = variant.strip().capitalize()
    data["vin"] = get_value_from_xpath(source, XPATHS["page_1"]["vin"])
    data["type"] = get_value_from_xpath(source, XPATHS["page_1"]["type"])
    data["last_update"] = get_value_from_xpath(source, XPATHS["page_1"]["last_update"]).split(" ")[-1]
    data["registration_number"] = get_value_from_xpath(source, XPATHS["page_1"]["registration_number"])
    data["first_registration"] = get_value_from_xpath(source, XPATHS["page_1"]["first_registration"])
    data["use"] = get_value_from_xpath(source, XPATHS["page_1"]["use"])
    data["vehicle_id"] = get_value_from_xpath(source, XPATHS["page_1"]["vehicle_id"])
    data["color"] = get_value_from_xpath(source, XPATHS["page_1"]["color"])
    data["model_year"] = get_value_from_xpath(source, XPATHS["page_1"]["model_year"])
    return data

# page title is "2. Tekniske oplysninger"
def page_2(source):
    data = dict()
    data["total_weight"] = get_value_from_xpath(source, XPATHS["page_2"]["total_weight"])
    data["vehicle_weight"] = get_value_from_xpath(source, XPATHS["page_2"]["vehicle_weight"])
    data["propulsion"] = get_value_from_xpath(source, XPATHS["page_2"]["propulsion"])
    data["tow_bar"] = get_value_from_xpath(source, XPATHS["page_2"]["tow_bar"])
    data["fuel_consumption"] = get_value_from_xpath(source, XPATHS["page_2"]["fuel_consumption"])
    data["cylinders"] = get_value_from_xpath(source, XPATHS["page_2"]["cylinders"])
    data["plugin_hybrid"] = get_value_from_xpath(source, XPATHS["page_2"]["plugin_hybrid"])
    data["electricity_consumption"] = get_value_from_xpath(source, XPATHS["page_2"]["electricity_consumption"])
    data["electric_range"] = get_value_from_xpath(source, XPATHS["page_2"]["electric_range"])
    data["battery_capacity"] = get_value_from_xpath(source, XPATHS["page_2"]["battery_capacity"])
    data["body_type"] = get_value_from_xpath(source, XPATHS["page_2"]["body_type"])
    data["particle_filter"] = get_value_from_xpath(source, XPATHS["page_2"]["particle_filter"])
    data["doors"] = get_value_from_xpath(source, XPATHS["page_2"]["doors"])
    return data

# Page 3: "Syn"


# Page 4: "Forsikring"
def page_4(source):
    data = {"insurance": {}}
    data["insurance"]["company"] = get_value_from_xpath(source, XPATHS["page_4"]["company"])
    data["insurance"]["is_active"] = True if get_value_from_xpath(source, XPATHS["page_4"]["is_active"]) == "Aktiv" else False
    data["insurance"]["number"] = None if get_value_from_xpath(source, XPATHS["page_4"]["number"]) == "N/A" else get_value_from_xpath(source, XPATHS["page_4"]["number"])
    data["insurance"]["created"] = get_value_from_xpath(source, XPATHS["page_4"]["created"])
    return data