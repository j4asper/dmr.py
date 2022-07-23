def clean(data):
    for key, value in data.items():
        if value.startswith("-"):
            data[key] = None
        if value == "Nej":
            data[key] = False
        if value == "Ja":
            data[key] = True
    return data