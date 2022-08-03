# xpaths for the different elements on the site
XPATHS = {
    "page_1": {
        "make_model_variant": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/span[2]",
        "vin": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/span[2]",
        "type": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[3]/span[2]",
        "last_update": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div[4]/span[2]",
        "registration_number": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/span[2]",
        "first_registration": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[2]/span",
        "use": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/span[2]",
        "vehicle_id": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[2]/span",
        "color": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[3]/div[2]/span",
        "model_year": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[4]/div[2]/span",
    },
    
    "page_2": {
        "total_weight": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/span[1]",
        "vehicle_weight": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]/span[1]",
        "propulsion": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div[2]/div[2]/span",
        "tow_bar": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div[3]/div[2]/span",
        "fuel_consumption": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[1]/div[2]/span[1]",
        "cylinders": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[2]/span",
        "plugin_hybrid": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div[3]/div[2]/span",
        "electricity_consumption": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[1]/div[2]/div[2]/span[1]",
        "electric_range": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[2]/div[2]/span",
        "battery_capacity": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[4]/div/div[2]/div[3]/div[2]/span",
        "body_type": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[6]/div/div[1]/div[1]/div[2]/span",
        "particle_filter": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[8]/div/div[1]/fieldset/div[6]/div[2]/span",
        "doors": "/html/body/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[6]/div/div[1]/div[3]/div[2]/span",
    },
    
    "page_3": None,
    
    "page_4": {
        "company": '//*[@id="lblSelskab"]',
        "is_active": '//*[@id="lblStatus"]',
        "number": '//*[@id="lblBevisNummer"]',
        "created": '//*[@id="lblbevisdato"]',
    },
}