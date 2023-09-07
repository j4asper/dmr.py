from enum import Enum


class UseType(str, Enum):
    """The use type that the vehicle is used for"""
    special_use = "Særlig anvendelse"
    private_driving = "Privat personkørsel"
    residence = "Beboelse"
    freight_transport_half_oms = "Godstransport (½ OMS.)"
    freight_transport_business = "Godstransport erhverv"
    freight_transport_private_and_business = "Godstransport privat/erhverv"
    freight_transport_private = "Godstransport privat"
    limousine_driving = "Limousinekørsel"
    public_authority_driving = "Kørsel for offentlig myndighed"
    freight_transport = "Godstransport"
    taxi_driving = "Taxikørsel"
    medical_transport = "Sygetransport"
    private_bus_driving = "Privat buskørsel"
