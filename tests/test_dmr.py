from datetime import datetime
from dmr import DMR

def test_get_by_plate():
    """Tests the scraper by getting data from one licens plate and check with the expected values"""
    dmr_obj = DMR().get_by_plate(license_plate="cw87553")
    
    assert dmr_obj.make == "Suzuki"
    assert dmr_obj.first_registration == datetime(2005, 8, 22, 0, 0)
    assert dmr_obj.vin == "TSMMZC21S00122899"