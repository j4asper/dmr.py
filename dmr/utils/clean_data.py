from datetime import datetime

def clean(data):
    for key, value in data.items():
        if value.startswith("-"):
            data[key] = None
        if value == "Nej":
            data[key] = False
        if value == "Ja":
            data[key] = True
        if value == "Ukendt":
            data[key] = None
        if key == "last_update" or key == "first_registration":
            data[key] = datetime.strptime(value, "%d-%m-%Y")
    return data