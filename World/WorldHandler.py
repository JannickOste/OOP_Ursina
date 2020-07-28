from ursina import *
from copy import copy

from packets import Player
from World import Tile


class WorldHandler(Entity):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.terain_mesh, self.player =  self.__generate_terain(), self.__set_player()
        self.tiles = []

    def __generate_terain(self):
        c = Cylinder(8, height=1, start=1)
        vertices, colors = ([], [])

        size = 16

        for z in range(size):
            for x in range(size):
                for y in range(1):
                    tile_voxel = Tile(world=self, color=color.black, position=(x, y, z))

                    tile_voxel.collider = MeshCollider(tile_voxel, mesh=c, center=-tile_voxel.origin)
                    top = Entity(parent=tile_voxel, model=copy(c), y=1.01, scale_y=.01)
                    top.color = lerp(color.lime, color.random_color(), .2)

        return Mesh(vertices, colors=colors)

    def __set_player(self):
        Entity(model='quad', scale=99999, color=color.azure.tint(-.1), rotation_x=90)
        player = Player()
        return player
