from pconf.settings import binder
import pytest


@binder(api2="root/api/api2")
def main(api1, api2):
    assert api1 == 'api1'
    assert api2 == 'api2'


@binder(api2="root/api/api2")
def main2(api2):
    return api2


def test_decorator():
    main("api1")


def test_decorator2():
    assert main2() == "api2"
