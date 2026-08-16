"""
Project Configuration
Hand Gesture Recognition Project
"""

# ===============================
# Camera Settings
# ===============================

CAMERA_INDEX = 0
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 30

# ===============================
# Hand Tracking
# ===============================

MAX_HANDS = 2
SMOOTH_ALPHA = 0.7

# ===============================
# Gesture Recognition
# ===============================

GESTURE_CONFIDENCE = 0.70

# ===============================
# Energy System
# ===============================

MAX_ENERGY = 100
ENERGY_REGEN_RATE = 0.5

# ===============================
# Animation
# ===============================

TRAIL_LENGTH = 12
PARTICLE_POOL_SIZE = 150
SMOKE_POOL_SIZE = 80
SPARK_POOL_SIZE = 80

# ===============================
# Fireball
# ===============================

FIREBALL_SPEED = 18
FIREBALL_MAX_DISTANCE = 500

# ===============================
# Shield
# ===============================

SHIELD_RADIUS = 80

# ===============================
# HUD
# ===============================

HUD_COLOR = (0, 255, 255)
TEXT_COLOR = (255, 255, 255)

# ===============================
# Performance
# ===============================

SHOW_FPS = True
ENABLE_MOTION_BLUR = False
ENABLE_CAMERA_SHAKE = False
ENABLE_CAMERA_ZOOM = False
ENABLE_VIGNETTE = False

# ===============================
# Debug
# ===============================

DEBUG = False
SHOW_LANDMARKS = True
SHOW_PROFILER = False

# ===============================
# Power Settings
# ===============================

SHIELD_ENERGY = 0.3
LASER_ENERGY = 0.3
LIGHTNING_ENERGY = 0.3
ICE_ENERGY = 0.2
SPIDER_ENERGY = 8
FIREBALL_ENERGY = 10
EXPLOSION_ENERGY = 15

FIST_COOLDOWN = 1.0
THUMBS_UP_COOLDOWN = 0.5
SPIDER_COOLDOWN = 0.3