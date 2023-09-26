from dmr import Converter


def test_km_to_miles():
    assert Converter.km_to_miles(17) == 10.56


def test_miles_to_km():
    assert Converter.miles_to_km(17) == 27.36


def test_kg_to_lb():
    assert Converter.kg_to_lb(17) == 37.48


def test_lb_to_kg():
    assert Converter.lb_to_kg(17) == 7.71
