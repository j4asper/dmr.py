from datetime import datetime
from time import sleep
from dmr import DMR
import asyncio

def test_validate_license_plate():
    """Test license plate validator"""
    is_license_plate = DMR().validate_license_plate("GGGGGGG")
    assert is_license_plate == True
    
    is_license_plate = DMR().validate_license_plate("ThisIsNotReal")
    assert is_license_plate == False

def test_get_by_plate():
    """Tests the scraper by getting data from a list of licens plates and check with the expected values"""

    # Test non-existing license plate
    dmr_obj = DMR().get_by_plate(license_plate="GGGGGGG")
    assert dmr_obj is None

    expected_data = {
        "cw87553": {
            "make": "Suzuki",
            "model": "Swift",
            "variant": "1,5",
            "vin": "TSMMZC21S00122899",
            "type": "Personbil",
            "last_update": datetime(2021, 1, 15, 0, 0),
            "registration_number": "CW87553",
            "first_registration": datetime(2005, 8, 22, 0, 0),
            "use": "Privat personkørsel",
            "vehicle_id": 1025401200519987,
            "color": None,
            "model_year": None,
            "total_weight": 1475,
            "vehicle_weight": 950,
            "propulsion": "Benzin",
            "tow_bar": False,
            "fuel_consumption": 15.4,
            "cylinders": None,
            "plugin_hybrid": None,
            "electricity_consumption": None,
            "electric_range": None,
            "battery_capacity": None,
            "body_type": None,
            "particle_filter": False,
            "doors": None,
            "insurance": {"company": "GF-FORSIKRING A/S",
                          "created": datetime(2022, 11, 8, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
        "ap43115": {
            "make": "Tesla",
            "model": "Model s",
            "variant": "85p",
            "vin": "5YJSA6H13EFP52466",
            "type": "Personbil",
            "last_update": datetime(2014, 12, 1, 0, 0),
            "registration_number": "AP43115",
            "first_registration": datetime(2014, 12, 1, 0, 0),
            "use": "Privat personkørsel",
            "vehicle_id": 9000000000998775,
            "color": "Sort",
            "model_year": 2014,
            "total_weight": 2590,
            "vehicle_weight": None,
            "propulsion": "El",
            "tow_bar": False,
            "fuel_consumption": None,
            "cylinders": 0,
            "plugin_hybrid": None,
            "electricity_consumption": 181.0,
            "electric_range": None,
            "battery_capacity": None,
            "body_type": "Hatchback",
            "particle_filter": None,
            "doors": 5,
            "insurance": {"company": "GF-FORSIKRING A/S",
                          "created": datetime(2020, 9, 5, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
        "dd24506": {
            "make": "Mg",
            "model": "Ehs plug-in hybrid",
            "variant": "1.5 5-dørs aut. 6",
            "vin": "LSJA24397MN069226",
            "type": "Personbil",
            "last_update": datetime(2021, 9, 16, 0, 0),
            "registration_number": "DD24506",
            "first_registration": datetime(2021, 9, 16, 0, 0),
            "use": "Privat personkørsel",
            "vehicle_id": 9000000004179000,
            "color": "Sort",
            "model_year": 2021,
            "total_weight": 2196,
            "vehicle_weight": None,
            "propulsion": "Benzin",
            "tow_bar": False,
            "fuel_consumption": 66.7,
            "cylinders": 4,
            "plugin_hybrid": True,
            "electricity_consumption": 198.3,
            "electric_range": 52.0,
            "battery_capacity": 12.5,
            "body_type": "Hatchback",
            "particle_filter": False,
            "doors": 5,
            "insurance": {"company": "ABC for Eir Försäkring AB",
                          "created": datetime(2022, 6, 4, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
        "cy41511": {
            "make": "Toyota",
            "model": "Mirai",
            "variant": "1.8 brint-hybrid sedan aut. gear",
            "vin": "JTDAABAA80A000567",
            "type": "Personbil",
            "last_update": datetime(2021, 3, 9, 0, 0),
            "registration_number": "CY41511",
            "first_registration": datetime(2021, 3, 9, 0, 0),
            "use": "Privat personkørsel",
            "vehicle_id": 9000000003963744,
            "color": "Blå",
            "model_year": 2021,
            "total_weight": 2415,
            "vehicle_weight": None,
            "propulsion": "Brint",
            "tow_bar": False,
            "fuel_consumption": None,
            "cylinders": 0,
            "plugin_hybrid": False,
            "electricity_consumption": None,
            "electric_range": None,
            "battery_capacity": None,
            "body_type": "Sedan  ",
            "particle_filter": False,
            "doors": 4,
            "insurance": {"company": "GJENSIDIGE FORSIKRING",
                          "created": datetime(2022, 3, 31, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
        "ap22698": {
            "make": "Fiat",
            "model": "Scudo",
            "variant": "2.0 mjt 165 kassevogn",
            "vin": "ZFA27000064355698",
            "type": "Varebil",
            "last_update": datetime(2014, 12, 23, 0, 0),
            "registration_number": "AP22698",
            "first_registration": datetime(2014, 12, 23, 0, 0),
            "use": "Godstransport privat/erhverv",
            "vehicle_id": 9000000001018398,
            "color": None,
            "model_year": 2011,
            "total_weight": 2973,
            "vehicle_weight": None,
            "propulsion": "Diesel",
            "tow_bar": True,
            "fuel_consumption": 14.7,
            "cylinders": 4,
            "plugin_hybrid": None,
            "electricity_consumption": None,
            "electric_range": None,
            "battery_capacity": None,
            "body_type": None,
            "particle_filter": True,
            "doors": 3,
            "insurance": {"company": "TRYG FORSIKRING A/S",
                          "created": datetime(2022, 8, 8, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
        "ca20548": {
            "make": "Yamaha",
            "model": "Yzf",
            "variant": "R 1",
            "vin": "TP1224102800",
            "type": "Motorcykel",
            "last_update": datetime(2019, 3, 16, 0, 0),
            "registration_number": "CA20548",
            "first_registration": datetime(2000, 8, 3, 0, 0),
            "use": "Privat personkørsel",
            "vehicle_id": 9000000002356860,
            "color": None,
            "model_year": None,
            "total_weight": 395,
            "vehicle_weight": 198,
            "propulsion": "Benzin",
            "tow_bar": False,
            "fuel_consumption": None,
            "cylinders": 4,
            "plugin_hybrid": None,
            "electricity_consumption": None,
            "electric_range": None,
            "battery_capacity": None,
            "body_type": None,
            "particle_filter": None,
            "doors": None,
            "insurance": {"company": "GJENSIDIGE FORSIKRING",
                          "created": datetime(2021, 3, 19, 0, 0),
                          "is_active": True,
                          "number": None
            }
        },
    }

    for license_plate in expected_data.keys():
        if list(expected_data).index(license_plate) <= 3:
            # Async test
            loop = asyncio.new_event_loop()
            dmr_obj = loop.run_until_complete(DMR(license_plate).get_by_plate_async())
        else:
            # Sync test
            dmr_obj = DMR(license_plate).get_by_plate()

        assert dmr_obj.raw_data == expected_data[license_plate]

        sleep(3)
