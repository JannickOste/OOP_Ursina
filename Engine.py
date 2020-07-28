from ursina import Ursina, application

from Settings import Settings
from World import WorldHandler
from packets import Camera


class Engine(Ursina):
    def __init__(self, app):
        super(Engine, self).__init__()
        self.applet = application
        self.settings = Settings(app=app)

        self.world, self.camera = (None, None)

    def _init_components(self):
        self.world = WorldHandler()
        self.camera = Camera(app=self)
