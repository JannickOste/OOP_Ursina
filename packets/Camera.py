from ursina import Entity, color, camera


class Camera(Entity):
    def __init__(self, **kwargs):
        super(Camera, self).__init__()
        self.cursor = None
        self.cursor_color = color.white

    def __set_cursor(self):
        return Entity(
            parent=camera.ui,
            model="quad",
            color=self.cursor_color,
            scale=.008,
            rotation_z=45
        )

    def update(self):
        self.cursor = self.__set_cursor()