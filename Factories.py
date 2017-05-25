from Products import *
from MusikdatenbankFabrik import *
import os

class MockupFactory(MusikdatenbankFabrik):
    """
    Die Factory Klasse fügt die Products in die Paylist hinein!
    """
    def __init__(self):
        super(MockupFactory, self).__init__()

    def load(self):
        """
        Mit dieser Methode werden Products in die Queue hineingefügt!
        :return:
        """
        self.queue.append(MockupProduct())


#Bei dieser Klasse habe ich wieder Hilfe von meinem Kollegen Wellner erhalten!
class FileFactory(MusikdatenbankFabrik):
    """
    Die Lieder (bzw. mp3 Dateien) werden in die Playlist hinzugefügt!
    """

    def __init__(self):
        super(FileFactory, self).__init__()


    def load(self):
        """
        Die Lieder werden in die Queue hinzugefügt!
        :return:
        """
        for lied in os.listdir("lieder"):
            if lied[-3:].lower() in ["mpr3"]:
                self.queue.append(FileProduct("lieder/" + lied))

