from .expected_data import expected_data
from time import sleep
from dmr import DMR
import asyncio


def get_object_for_comparison(license_plate, test_async: bool):
    if test_async:
        loop = asyncio.new_event_loop()
        vehicle = loop.run_until_complete(DMR.get_by_plate_async(license_plate))
    else:
        vehicle = DMR.get_by_plate(license_plate)
    
    sleep(3)
    
    return vehicle, expected_data[license_plate]


def validate_object(dmr, expected):
    assert dmr.make == expected["make"]
    assert dmr.model == expected["model"]
    assert dmr.variant == expected["variant"]
    assert dmr.vin == expected["vin"]
    assert dmr.type == expected["type"]
    assert dmr.last_update == expected["last_update"]
    assert dmr.registration_number == expected["registration_number"]
    assert dmr.first_registration == expected["first_registration"]
    assert dmr.use == expected["use"]
    assert dmr.vehicle_id == expected["vehicle_id"]
    assert dmr.color == expected["color"]
    assert dmr.model_year == expected["model_year"]
    assert dmr.total_weight == expected["total_weight"]
    assert dmr.vehicle_weight == expected["vehicle_weight"]
    assert dmr.propulsion == expected["propulsion"]
    assert dmr.tow_bar == expected["tow_bar"]
    assert dmr.fuel_consumption == expected["fuel_consumption"]
    assert dmr.cylinders == expected["cylinders"]
    assert dmr.plugin_hybrid == expected["plugin_hybrid"]
    assert dmr.electricity_consumption == expected["electricity_consumption"]
    assert dmr.electric_range == expected["electric_range"]
    assert dmr.battery_capacity == expected["battery_capacity"]
    assert dmr.body_type == expected["body_type"]
    assert dmr.particle_filter == expected["particle_filter"]
    assert dmr.doors == expected["doors"]
    assert dmr.insurance.company == expected["insurance"]["company"]
    assert dmr.insurance.created == expected["insurance"]["created"]
    assert dmr.insurance.is_active == expected["insurance"]["is_active"]
    assert dmr.insurance.number == expected["insurance"]["number"]