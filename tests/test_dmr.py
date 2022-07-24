from datetime import datetime
from dmr import DMR

def test_get_by_plate():
    """Tests the scraper by getting data from one licens plate and check with the expected values"""
    dmr_obj = DMR().get_by_plate(license_plate="cw87553")
    
    assert dmr_obj.make == "Suzuki"
    assert dmr_obj.propulsion == "Benzin"
    assert dmr_obj.fuel_consumption == 15.4
    assert dmr_obj.tow_bar == False
    assert dmr_obj.vehicle_weight == 950
    assert dmr_obj.total_weight == 1475
    assert dmr_obj.particle_filter == False
    assert dmr_obj.first_registration == datetime(2005, 8, 22, 0, 0)
    assert dmr_obj.vin == "TSMMZC21S00122899"
    assert dmr_obj.type == "Personbil"