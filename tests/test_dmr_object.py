from .helper_methods import get_object_for_comparison, validate_object


def test_dmr_object_normal_car():
    dmr, expected = get_object_for_comparison("cw87553", False)
    validate_object(dmr, expected)


def test_dmr_object_electric_car():
    dmr, expected = get_object_for_comparison("ap43115", False)
    validate_object(dmr, expected)


def test_dmr_object_plugin_hybrid_car():
    dmr, expected = get_object_for_comparison("dd24506", False)
    validate_object(dmr, expected)


def test_dmr_object_hydrogen_car():
    dmr, expected = get_object_for_comparison("cy41511", False)
    validate_object(dmr, expected)


def test_dmr_object_van():
    dmr, expected = get_object_for_comparison("ap22698", False)
    validate_object(dmr, expected)


def test_dmr_object_motorcycle():
    dmr, expected = get_object_for_comparison("ca20548", False)
    validate_object(dmr, expected)
