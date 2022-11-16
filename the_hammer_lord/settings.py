SCREEN_SIZE = 1366, 768

TARGET_FRAMERATE = 60

SCALE_RATIO = 4

CAMERA_SPEED = 15
PLAYER_SPEED_HORIZONTAL = 5
PLAYER_JUMPING_MOMENTUM = 15

GRAVITY_FORCE = 0.03

PLAYER_SPRITE_WIDTH = 80
PLAYER_SPRITE_HEIGHT = 64
PLAYER_SHIFT_FROM_CENTER_X = 70  # to center the player without hammer
PLAYER_SHIFT_FROM_CENTER_Y = 0
PLAYER_ANIMATION_COOLDOWN = 350
PLAYER_HEALTH = 300
PLAYER_COORDS_CENTERED = (
    SCREEN_SIZE[0] // 2 + PLAYER_SHIFT_FROM_CENTER_X,
    SCREEN_SIZE[1] // 2 + PLAYER_SHIFT_FROM_CENTER_Y,
)

MAGIC_COLLISION_SHIFT = 1

ENEMY_TEST_RECT_SIZE = 100, 150
ENEMY_SPEED = 2
ENEMY_HEALTH = 100

HEALTH_BAR_THICKNESS = 3
