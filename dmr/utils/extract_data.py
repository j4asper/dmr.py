# Landing page when looking up a licens plate, the page title is "1. Køretøj"
def page_1(source):
    data = dict()
    make, model, variant = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span[2]')[0].text_content().split(",", 2)
    data["make"], data["model"], data["variant"] = make.strip().lower().capitalize(), model.strip().lower().capitalize(), variant.strip().lower().capitalize()
    data["vin"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/span[2]')[0].text_content()
    data["type"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[3]/span[2]')[0].text_content()
    data["last_update"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[4]/span[2]')[0].text_content().split(" ")[-1]
    data["registration_number"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/span[2]')[0].text_content()
    data["first_registration"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/span')[0].text_content()
    data["use"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/span[2]')[0].text_content()
    data["vehicle_id"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[2]/span')[0].text_content()
    data["color"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[3]/div[2]/span')[0].text_content()
    data["model_year"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[4]/div[2]/span')[0].text_content()
    # data[""] = source.xpath('')[0].text_content()
    return data

# page title is "2. Tekniske oplysninger"
def page_2(source):
    data = dict()
    data["total_weight"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/span[1]')[0].text_content()
    data["vehicle_weight"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]/span[1]')[0].text_content()
    data["propulsion"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/span')[0].text_content()
    data["tow_bar"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]/span')[0].text_content()
    data["fuel_consumption"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[2]/span[1]')[0].text_content()
    data["cylinders"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/span')[0].text_content()
    data["plugin_hybrid"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/div[2]/span')[0].text_content()
    data["electricity_consumption"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[2]/div[2]/span[1]')[0].text_content()
    data["electric_range"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/span')[0].text_content()
    data["battery_capacity"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[3]/div[2]/span')[0].text_content()
    data["body_type"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[6]/div/div[1]/div[1]/div[2]/span')[0].text_content()
    data["particle_filter"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[8]/div/div[1]/fieldset/div[6]/div[2]/span')[0].text_content()
    data["doors"] = source.xpath('/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[6]/div/div[1]/div[3]/div[2]/span')[0].text_content()
    return data
