from pconf.settings import Pconf
import pytest

def test_configuration():
    conf = Pconf(__file__)

    api1_value = conf.get('root/api/api1')
    assert api1_value == 'value1'

    api2_value = conf.get('api2')
    assert api2_value == 'value2'
