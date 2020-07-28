from ursina import Ursina, application, mouse

from Settings import Settings
from world import WorldHandler
from packets import Camera


class Engine(Ursina):
    def __init__(self, app):
        super(Engine, self).__init__()
        self.applet = application
        self.settings = Settings(app=app)
        self.world, self.camera = (None, None)
        mouse.locked = True

    def _init_components(self):
        self.world = WorldHandler(app=self)
        self.camera = Camera(app=self)