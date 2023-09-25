from dmr import DMR
import asyncio


def test_validate_license_plate():
    """Test license plate validator"""
    is_license_plate = DMR.validate_license_plate("GGGGGGG")
    assert is_license_plate == True

    is_license_plate = DMR.validate_license_plate("ThisIsNotReal")
    assert is_license_plate == False


def test_invalid_license_plate():
    dmr_obj = DMR.get_by_plate(license_plate="GGGGGGG")
    assert dmr_obj is None

def test_invalid_license_plate_async():
    loop = asyncio.new_event_loop()
    dmr_obj = loop.run_until_complete(DMR.get_by_plate_async("GGGGGGG"))
    assert dmr_obj is None
