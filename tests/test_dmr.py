from dmr import DMR

def test_get_by_plate():
    """Tests the scraper by getting data from one licens plate and check with the expected values"""
    dmr_obj = DMR().get_by_plate(license_plate="cw87553")
    
    assert dmr_obj.make == "Suzuki"