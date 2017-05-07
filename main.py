from factory_musikdatenbank.MusikdatenbankMockupFabrik import *
from factory_musikdatenbank.MusikdatenbankFileFabrik import *

__author__ = 'DD'

if __name__ == '__main__':
    fabrik = MusikdatenbankFileFabrik()
    #fabrik = MusikdatenbankMockupFabrik()
    fabrik.abspielen()