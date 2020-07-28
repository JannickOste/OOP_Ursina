from ursina import Entity, color, camera, LVector3f, mouse, clamp


class Camera(Entity):
    def __init__(self, app):
        super(Camera, self).__init__()
        self.cursor = None
        self.cursor_color = color.white
        self.direction = LVector3f(0, 0, 0)
        self.app = app

        camera.parent = app.world.player
        camera.rotation = (0, 0, 0)
        camera.position = (0, 1.5, 0)
        camera.fov = 90

    def __set_cursor(self):
        return Entity(
            parent=camera.ui,
            model="quad",
            color=self.cursor_color,
            scale=.008,
            rotation_z=45
        )

    def __get_movement(self):
        # Get camera movement currently player only
        self.app.world.player.rotation_y += mouse.velocity[0] * 30
        camera.rotation_x -= mouse.velocity[1] * 40

        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

    def update(self):
        self.cursor = self.__set_cursor()
        self.__get_movement()