from datetime import datetime

def clean(data):
    for key, value in data.items():
        if value.startswith("-") or value == "Ukendt":
            data[key] = None
            continue
        if value == "Nej" or value == "Ja":
            data[key] = True if value == "Ja" else False
            continue
        if key == "last_update" or key == "first_registration":
            data[key] = datetime.strptime(value, "%d-%m-%Y")
            continue
        if  any(key==ckey for ckey in ["fuel_consumption", "electricity_consumption", "battery_capacity", "electric_range"]):
            value = value.replace(",", ".")
            try:
                value = float(value)
                data[key] = float(value)
                continue
            except ValueError:
                pass
        if value.isnumeric():
            data[key] = int(value)
    return data