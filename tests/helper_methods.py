from .expected_data import expected_data
from time import sleep
from dmr import DMR
import asyncio

def get_data_for_comparison(license_plate, test_async:bool):
    if test_async:
        loop = asyncio.new_event_loop()
        dmr_obj = loop.run_until_complete(DMR(license_plate).get_by_plate_async())
    else:
        dmr_obj = DMR(license_plate).get_by_plate()
    
    sleep(3)
    
    return dmr_obj.raw_data, expected_data[license_plate]

def get_object_for_comparison(license_plate, test_async:bool):
    if test_async:
        loop = asyncio.new_event_loop()
        dmr_obj = loop.run_until_complete(DMR(license_plate).get_by_plate_async())
    else:
        dmr_obj = DMR(license_plate).get_by_plate()
    
    sleep(3)
    
    return dmr_obj, expected_data[license_plate]