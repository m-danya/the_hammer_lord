from pygame import Surface, image, transform

from the_hammer_lord.types import Size2D, Point, Vector2D
from the_hammer_lord.level.border_surface import (
    BorderSurface,
    BorderSurfaceType,
)
from the_hammer_lord.entities.player import Player
from the_hammer_lord.ui.debug_info_corner import DebugInfoCorner
from the_hammer_lord.utils.camera import Camera
from the_hammer_lord.utils.collidables_storage import CollidablesStorage
from the_hammer_lord.assets.sprites import SPRITES


class Level:
    # top left corner is (0, 0) in level coordinate system
    _size: Size2D
    _floor: BorderSurface
    _ceiling: BorderSurface
    _left_border: BorderSurface
    _right_border: BorderSurface
    _camera: Camera
    _collidablesStorage: CollidablesStorage
    _player: Player
    _level_bg: Surface
    _debug_info_corner: DebugInfoCorner

    def __init__(self, level_size: Size2D = (3840, 1200)):
        self._size = level_size
        self._camera = Camera(1200, 88)
        self._collidablesStorage = CollidablesStorage()
        self._debug_info_corner = DebugInfoCorner(self)

    # generates the structure of the level, different params could be passed in the future
    def generate(self):
        self._level_bg = image.load(SPRITES["LevelBackground1"]).convert_alpha()
        self._level_bg = transform.scale(self._level_bg, self._size)
        self._floor = BorderSurface(
            BorderSurfaceType.FLOOR,
            self._size,
            forming_points_list=[
                (0, 700),
                (420, 800),
                (800, 700),
                (1000, 600),
                (1200, 700),
                (1400, 800),
                (1700, 900),
                (1800, 1000),
                (1900, 1100),
                (2600, 1200),
                (2950, 1000),
            ],
        )
        self._ceiling = BorderSurface(
            BorderSurfaceType.CEILING,
            self._size,
            forming_points_list=[
                (0, 250),
                (700, 300),
                (1700, 400),
                (1800, 450),
                (1900, 500),
                (2800, 600),
            ],
        )
        self._left_border = BorderSurface(
            BorderSurfaceType.LEFT_BORDER,
            self._size,
            forming_points_list=[
                (100, 0),
            ],
        )
        self._right_border = BorderSurface(
            BorderSurfaceType.RIGHT_BORDER,
            self._size,
            forming_points_list=[
                (self._size[0] - 100, 0),
            ],
        )
        self._collidablesStorage.extend(
            [self._floor, self._ceiling, self._left_border, self._right_border]
        )

    # creates new player on the level (could be used in reset)
    def spawn_player(self, pos: Point = (900, 400)):
        self._player = Player(pos)

    def setup(self, *args, **kwargs):
        self.generate()
        self.spawn_player()
        self._camera.bind_player(self._player)

    def reset(self):
        pass

    # called in the main event loop
    def update(self, display: Surface, motion_vector: Vector2D):
        # render level background
        display.blit(self._level_bg, self._camera.calc_render_coords((0, 0)))
        self._floor.render(display, self._camera)
        self._ceiling.render(display, self._camera)
        self._left_border.render(display, self._camera)
        self._right_border.render(display, self._camera)
        self._player.update(
            display,
            self._camera.calc_render_coords(
                (self._player.rect.x, self._player.rect.y)
            ),
        )
        self._player.move(motion_vector, self._collidablesStorage)
        self._camera.detect_locked_axes(self._size)
        self._camera.move()
        self._debug_info_corner.update(display)
