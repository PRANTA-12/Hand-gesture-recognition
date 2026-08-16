from dataclasses import dataclass


@dataclass
class AppContext:
    # ===============================
    # Camera / Detection
    # ===============================

    detector: object = None

    # ===============================
    # Gesture System
    # ===============================

    gesture_pipeline: object = None
    left_processor: object = None
    right_processor: object = None

    # ===============================
    # Pipelines
    # ===============================

    power_pipeline: object = None
    animation_pipeline: object = None
    render_pipeline: object = None

    # ===============================
    # Managers
    # ===============================

    animation_manager: object = None
    effect_manager: object = None
    render_manager: object = None

    # ===============================
    # Controllers
    # ===============================

    power_controller: object = None
    two_hand_controller: object = None
    portal_controller: object = None

    # ===============================
    # Effects
    # ===============================

    particle_engine: object = None
    advanced_particles: object = None
    physics_engine: object = None

    # ===============================
    # Powers
    # ===============================

    fireball: object = None
    shield: object = None
    laser: object = None
    lightning: object = None
    ice: object = None
    spider_web: object = None
    explosion: object = None
    portal: object = None
    rasengan: object = None
    kamehameha: object = None

    # ===============================
    # Visual Effects
    # ===============================

    camera_shake: object = None
    camera_zoom: object = None
    motion_blur: object = None
    screen_flash: object = None
    visual_effects: object = None
    trail: object = None
    hud: object = None

    # ===============================
    # Gameplay
    # ===============================

    target_lock: object = None
    enemy: object = None

    # ===============================
    # Utilities
    # ===============================

    energy: object = None
    cooldown: object = None
    performance_monitor: object = None
    profiler: object = None
    frame_timer: object = None