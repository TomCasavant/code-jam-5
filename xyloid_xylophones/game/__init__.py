import pyglet
from pyqtree import Index
from config import *


# 640x640 makes it easier to draw tiles
game_window = pyglet.window.Window(width=game_width, height=game_height)

media = pyglet.media.Player()

#List of current pressed keys
keys = set()

class Base:
    id: int = 0
    name: str = 'base_class'
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    collision: bool = False


class Zone(Base):
    index: Index

    def __init__(self, index):
        self.index = index


# player object
class Player(Base):
    sprite: str = 'default_item'

    def __init__(self, name):
        self.name = name


class Item(Player):
    state: int = -1  # -1 intangible, 0 container unopened, 1 container opened
    sound: str = 'default_sound'
    contains: str = 'default_nothing'


class Resource:
    full_path: str = ''
    stream: None
    data: None


zone_map = {}
for i in zone_names:
    zone_map[i] = Zone(Index(bbox=(-1024, -1024, 1024, 1024)))
    zone_map[i].name = i

player = Player(player_name)
# static center of player square
player.center_x = 4*64
player.center_y = 4*64
# center of all the squares aka 0,0
player.x = zone_width // 2
player.y = zone_height // 2
player.width = sprite_width
player.height = sprite_height
# handlers for player movement
player.x_vel = 0
player.y_vel = 0

tick = 0
elapsed_time = 0

scene_list = {}
sound_list = {}
music_list = {}

current_display = "zone"
