from pconf.settings import configurate
import pytest


@configurate(api2 = "root/api/api2")
def main(api1, api2):
    assert api1 == 'api1'
    assert api2 == 'api2'

def test_decorator():
    main("api1")