from abc import ABCMeta, abstractmethod
import pyglet
import Products

__author__ = 'DD'

class MusikdatenbankFabrik(metaclass=ABCMeta):
    """ Die Basisklasse fuer Fabriken
    """

    def __init__(self):
        self.geladen = False
        self.queue = []


    def lade_musik(self):
        pass

    def play(self):
        if not self.geladen:
            self.load()
        for lied in self.queue:
            lied.play()

        pyglet.app.run()
        print('ENDE!')

    def exit_callback(self):
        pyglet.app.exit()