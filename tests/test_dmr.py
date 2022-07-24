from datetime import datetime
from dmr import DMR

def test_get_by_plate():
    """Tests the scraper by getting data from a list of licens plates and check with the expected values"""

    # Plate 1: Benzin car
    # Plate 2: Electric
    # Plate 3: Plug-in Hybrid

    expected_data = {
        "cw87553": {
            "make": "Suzuki",
            "propulsion": "Benzin",
            "fuel_consumption": 15.4,
            "tow_bar": False,
            "vehicle_weight": 950,
            "total_weight": 1475,
            "particle_filter": False,
            "first_registration": datetime(2005, 8, 22, 0, 0),
            "vin": "TSMMZC21S00122899",
            "type": "Personbil",
            "plugin_hybrid": None,
        },
        "ap43115": {
            "make": "Tesla",
            "propulsion": "El",
            "fuel_consumption": None,
            "tow_bar": False,
            "vehicle_weight": None,
            "total_weight": 2590,
            "particle_filter": None,
            "first_registration": datetime(2014, 12, 1, 0, 0),
            "vin": "5YJSA6H13EFP52466",
            "type": "Personbil",
            "plugin_hybrid": None,
        },
        "dd24506": {
            "make": "Mg",
            "propulsion": "Benzin",
            "fuel_consumption": 66.7,
            "tow_bar": False,
            "vehicle_weight": None,
            "total_weight": 2196,
            "particle_filter": False,
            "first_registration": datetime(2021, 9, 16, 0, 0),
            "vin": "LSJA24397MN069226",
            "type": "Personbil",
            "plugin_hybrid": True,
        }
    }
    
    for licens_plate in expected_data.keys():
        dmr_obj = DMR().get_by_plate(license_plate=licens_plate)
    
        assert dmr_obj.make == expected_data[licens_plate]["make"]
        assert dmr_obj.propulsion == expected_data[licens_plate]["propulsion"]
        assert dmr_obj.fuel_consumption == expected_data[licens_plate]["fuel_consumption"]
        assert dmr_obj.tow_bar == expected_data[licens_plate]["tow_bar"]
        assert dmr_obj.vehicle_weight == expected_data[licens_plate]["vehicle_weight"]
        assert dmr_obj.total_weight == expected_data[licens_plate]["total_weight"]
        assert dmr_obj.particle_filter == expected_data[licens_plate]["particle_filter"]
        assert dmr_obj.first_registration == expected_data[licens_plate]["first_registration"]
        assert dmr_obj.vin == expected_data[licens_plate]["vin"]
        assert dmr_obj.type == expected_data[licens_plate]["type"]
        assert dmr_obj.plugin_hybrid == expected_data[licens_plate]["plugin_hybrid"]
