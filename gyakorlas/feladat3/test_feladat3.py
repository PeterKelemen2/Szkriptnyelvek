from feladat2 import feladat2


def test_string_info():
    ures = feladat2.string_info("")
    ures_elvart = {"upper": 0,
                   "lower": 0,
                   "length": 0}

    assert ures == ures_elvart

    nem_figyelt = feladat2.string_info("1/!*")
    nem_figyelt_elvart = {
        "upper": 0,
        "lower": 0,
        "length": 4
    }
    assert nem_figyelt == nem_figyelt_elvart

    assert len(nem_figyelt.keys()) == 3
# pytest -v
