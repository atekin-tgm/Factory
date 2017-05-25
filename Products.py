from Musikstueck import *
import pyglet

#Diesen Tipp habe ich von meinem Kollegen Wellner!
player = pyglet.media.Player()
player.volume = 0.3

class MockupProduct(Musikstueck):
    """
    Die Mockup Produkte werden in dieser Klasse erstellt!
    """

    def __init__(self):
        super(MockupProduct, self).__init__("titel", "interpret", "album")

    def play(selfself):
        return

class FileProduct(Musikstueck):
    """
    Die Lieder werden in dieser Klasse gemanaged!
    """

    def __init__(self, name):
        super(FileProduct, self).__init__("titel", "interpret", "album")
        self.name = name
        self.lied = pyglet.media.load(self.name)

    def play(self):
        """
        Der Player bekommt durch die play-Methode die Lieder um sie abzuspielen!
        :return:
        """
        player.queue(self.lied)
        player.play()
