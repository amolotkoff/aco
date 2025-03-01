from pconf.settings import Pconf
import pytest



def test_configuration():
    conf = Pconf(__file__)

    assert conf.get('root/api/api1') == 'api1'
    assert conf.get('root/api/api2') == 'api2'
