from ursina import camera, Entity, color, mouse, held_keys, clamp, raycast, time


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 3

        self.direction, self.__is_jumping = None, False
        self.i = 0
        self.update_interval = 30
        self.graphics = self.__set_player_model()
        camera.parent = self

        self.position = (0, 0, 1)

        camera.rotation = (0, 0, 0)
        camera.position = (0, 1.5, 0)
        camera.fov = 90
        mouse.locked = True

    def __set_player_model(self):
        return Entity(
            name='player_graphics',
            parent=self,
            model='cube',
            origin=(0, -.5, 1),
            scale=(1, 1.8, 1),
        )

    def update(self):
        if self.i < self.update_interval:
            self.i += 1
            return

        # Walk forwards/backwards
        self.direction = self.__get_direction()
        self.__get_jump()

    def __get_direction(self):
        return (
                self.forward * (held_keys['z'] - held_keys['s'])
                + self.right * (held_keys['d'] - held_keys['q'])
        )

    def __get_jump(self):
        if not raycast(self.world_position + self.up, self.direction, .5).hit:
            self.position += self.direction * self.speed * time.dt

        self.rotation_y += mouse.velocity[0] * 30
        camera.rotation_x -= mouse.velocity[1] * 40

        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

        if held_keys['a'] and not self.__is_jumping:
            self.y += held_keys['a']
            self.__is_jumping = True
        else:
            if self.__is_jumping:
                print("player is jumping")

