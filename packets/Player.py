from ursina import Entity, held_keys, raycast, time, LVector3f, Vec3


class Player(Entity):
    def __init__(self, app):
        super().__init__()
        self.app = app

        # Speed attributes
        self.__movement_speed = 3

        # Jumping objects
        self.__is_jumping = False
        self.__is_falling = False
        self.__start_jump = Vec3(0, 0, 0)

        # Movement objects
        self.direction = LVector3f(0, 0, 0)

        # Graphical objects
        self.graphics = self.__set_player_model()

        # Update counter
        self.i = 0
        self.update_interval = 30

        self.position = (0, 0, 1)

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

        self.__get_movement()
        self.__get_jump()

    def __get_movement(self):
        self.direction = (
                self.forward * (held_keys['z'] - held_keys['s'])
                + self.right * (held_keys['d'] - held_keys['q'])
        )
        
        if not raycast(self.world_position + self.up, self.direction, .5).hit:
            self.position += self.direction * self.__movement_speed * time.dt

    def __get_jump(self):
        if held_keys['space'] and not self.__is_falling:
            self.__is_jumping = True
        elif self.__is_jumping and not held_keys["space"]:
            self.__is_falling = True

        jump_speed = 4
        if self.__is_falling:
            for pos in self.app.world.tile_positions:
                if self.y < 0 or raycast(self.position, pos).hit:
                    self.__is_falling = False
                    self.__is_jumping = False
                else:
                    self.y -= jump_speed/10 * time.dt
            return

        if self.__is_jumping:
            if self.y >= self.__start_jump[1]+0.5:
                self.__is_falling = True
            else:
                self.y += jump_speed*time.dt


