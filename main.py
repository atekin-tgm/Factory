from Factories import *

__author__ = 'DD'

#Die Main Klasse um den Musikplayer zu starten!
if __name__ == '__main__':
    fabrik = FileFactory()
    #fabrik = MockupFactory()
    fabrik.play()
