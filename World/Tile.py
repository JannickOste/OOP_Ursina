from ursina import Entity


class Tile(Entity):
    def __init__(self, world, color, position):
        super().__init__(
                        parent=world,
                        name='tile',
                        model="cube",
                        origin_y=-.5,
                        double_sided=True,
                        color=color,
                        index=position,
                        position=position
        )
