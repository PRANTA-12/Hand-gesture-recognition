import cv2
import random
import math
from energy_manager import EnergyManager
from hand_detector import HandDetector
from prediction_filter import PredictionFilter
from gesture_recognizer import GestureRecognizer
from gesture_manager import GestureManager
from ai_gesture import AIGestureRecognizer
from ai_stabilizer import AIStabilizer
from utils import calculate_fps
from motion_blur import MotionBlur
from effects import Effects
from powers.energy_ball import EnergyBall
from particles import ParticleEngine
from advanced_particles import AdvancedParticles
from powers.sparks import Sparks
from powers.smoke import Smoke
from powers.laser import Laser
from powers.shield import Shield
from animation_manager import AnimationManager
from gesture.gesture_transition import GestureTransition
from gesture.gesture_fusion import GestureFusion
from gesture.power_queue import PowerQueue
from powers.status_bar import StatusBar

from powers.explosion import Explosion
from powers.lightning import Lightning
from powers.spider_web import SpiderWeb
from powers.ice import Ice
from powers.fireball import Fireball
from light_trail import LightTrail
from powers.hud import HUD
from cooldown_manager import CooldownManager
from camera_shake import CameraShake
from screen_flash import ScreenFlash
from landmark_filter import LandmarkFilter
from gesture.gesture_stabilizer import GestureStabilizer
from hand_ring import HandRing
from camera_zoom import CameraZoom
from gesture_actions import GESTURE_ACTIONS
from gesture_lock import GestureLock
from power_controller import PowerController
from gesture_state_machine import GestureStateMachine
from gesture_state import GestureState
from performance_profiler import PerformanceProfiler
from visual_effects import VisualEffects
from hand_position import HandPosition
from hand_rotation import HandRotation
from render_manager import RenderManager
from effect_manager import EffectManager
from config import *
from logger import logger
from frame_timer import FrameTimer
from performance_monitor import PerformanceMonitor
from powers.target_lock import TargetLock
from enemy import Enemy
from powers.portal import Portal
from powers.portal_controller import PortalController
from powers.power_hud import PowerHUD
from powers.gesture_flash import GestureFlash
from powers.two_hand_power_controller import TwoHandPowerController
from powers.kamehameha import Kamehameha
from powers.gravity_orb import GravityOrb
from powers.arc_reactor import ArcReactor
from powers.dual_lightning import DualLightning
from powers.rasengan import Rasengan
from gesture.gesture_pipeline import GesturePipeline
from gesture.power_pipeline import PowerPipeline
from gesture.animation_pipeline import AnimationPipeline
from gesture.render_pipeline import RenderPipeline
from gesture.hand_processor import HandProcessor
from physics import PhysicsEngine
from powers.power_manager import PowerManager
from ai.prediction_buffer import PredictionBuffer
from ai.confidence_filter import ConfidenceFilter
from two_hand_gesture import (
    TwoHandGesture,
    TwoHandPower
)
from ai.dataset_collector import DatasetCollector
from powers.sound_manager import SoundManager
# ===============================
# Project Settings
# ===============================

alpha = SMOOTH_ALPHA
MAX_HANDS = 2






camera = cv2.VideoCapture(CAMERA_INDEX)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
camera.set(cv2.CAP_PROP_FPS, CAMERA_FPS)

if not camera.isOpened():
    logger.error("Camera could not be opened")
    exit()

logger.info("Camera opened successfully") 


detector = HandDetector()
gesture = GestureRecognizer()
ai_gesture = AIGestureRecognizer()
gesture_machine = GestureStateMachine()
gesture_lock = GestureLock()
transition = GestureTransition()
fusion = GestureFusion()
left_power_queue = PowerQueue()
right_power_queue = PowerQueue()
power_hud = PowerHUD()
status_bar = StatusBar()
gesture_flash = GestureFlash()
gesture_manager = GestureManager()
gesture_pipeline = GesturePipeline()
two_hand = TwoHandGesture()
ai_stabilizer = AIStabilizer()
prediction_filter = PredictionFilter()
effects = Effects()
effect_manager = EffectManager()
visual_effects = VisualEffects()
render_manager = RenderManager()
kamehameha = Kamehameha()
performance_monitor = PerformanceMonitor()

# ===============================
# Sound System (Phase 11 / Step 89)
# ===============================
sound_manager = SoundManager()

left_processor = HandProcessor()
right_processor = HandProcessor()

left_filter = LandmarkFilter(alpha=0.7)
right_filter = LandmarkFilter(alpha=0.7)

left_stabilizer = GestureStabilizer(history_size=5)
right_stabilizer = GestureStabilizer(history_size=5)


particle_engine = ParticleEngine()
advanced_particles = AdvancedParticles()

sparks = Sparks()
smoke = Smoke()
explosion = Explosion()

portal = Portal()
portal_controller = PortalController(portal, sound_manager)
rasengan = Rasengan()
gravity_orb = GravityOrb()
arc_reactor = ArcReactor()
dual_lightning = DualLightning()

laser = Laser()
shield = Shield()
lightning = Lightning()
ice = Ice()
spider_web = SpiderWeb()
fireball = Fireball()

power_manager = PowerManager()
collector = DatasetCollector()
left_confidence_filter = ConfidenceFilter(
    threshold=0.60
)

right_confidence_filter = ConfidenceFilter(
    threshold=0.60
)

left_prediction_buffer = PredictionBuffer(size=5)
right_prediction_buffer = PredictionBuffer(size=5)
two_hand_controller = TwoHandPowerController(
    power_manager
)

enemy = Enemy()

target_lock = TargetLock()

camera_shake = CameraShake()

screen_flash = ScreenFlash()

camera_zoom = CameraZoom()

motion_blur = MotionBlur()

frame_timer = FrameTimer()

fireball.particles = advanced_particles


trail = LightTrail()

animation_manager = AnimationManager()
render_manager.animation_manager = animation_manager

animation_manager.register("FIREBALL", fireball)
animation_manager.register("ICE", ice)
animation_manager.register("LIGHTNING", lightning)
animation_manager.register("SPIDER", spider_web)
animation_manager.register("SHIELD", shield)
animation_manager.register("LASER", laser)
animation_manager.register(
    "PORTAL",
    portal
)
animation_manager.register(
    "RASENGAN",
    rasengan
)
animation_manager.register(
    "KAMEHAMEHA",
    kamehameha
)
animation_manager.register(
    "GRAVITY_ORB",
    gravity_orb
)
animation_manager.register(
    "ARC_REACTOR",
    arc_reactor
)
animation_manager.register(
    "DUAL_LIGHTNING",
    dual_lightning
)
power_manager.register("PORTAL", portal)
power_manager.register("RASENGAN", rasengan)
power_manager.register("KAMEHAMEHA", kamehameha)
power_manager.register("GRAVITY_ORB", gravity_orb)
power_manager.register("ARC_REACTOR", arc_reactor)
power_manager.register("DUAL_LIGHTNING", dual_lightning)

power_manager.register("LASER", laser)
power_manager.register("SHIELD", shield)
power_manager.register("LIGHTNING", lightning)
power_manager.register("FIREBALL", fireball)
power_manager.register("ICE", ice)
power_manager.register("SPIDER", spider_web)


def fireball_explode(position):
    explosion.trigger(position)
    camera_shake.trigger()
    screen_flash.trigger()
    sound_manager.play_explosion()

fireball.on_explode = fireball_explode


cooldown = CooldownManager()
energy = EnergyManager()
hud = HUD()
physics_engine = PhysicsEngine()
fireball.set_physics_engine(
    physics_engine
)

explosion.set_physics_engine(
    physics_engine
)

physics_engine.add(
    fireball.physics
)

hand_ring = HandRing()

power_controller = PowerController(
    power_manager,
    animation_manager,
    shield,
    fireball,
    explosion,
    lightning,
    ice,
    spider_web,
    cooldown,
    energy,
    camera_zoom,
    camera_shake,
    screen_flash,
    target_lock,
    sound_manager
)

power_pipeline = PowerPipeline(
    power_controller,
    two_hand_controller,
    target_lock,
    fireball
)

animation_pipeline = AnimationPipeline(
    performance_monitor,
    particle_engine,
    advanced_particles,
    effect_manager,
    animation_manager,
    enemy,
    target_lock,
    camera_shake,
    camera_zoom,
    motion_blur,
    screen_flash
)
render_pipeline = RenderPipeline(
    render_manager,
    hud,
    visual_effects,
    performance_monitor
)

def process_hand(
    handData,
    queue,
    prediction_buffer,
    confidence_filter,
    stabilizer
):

    if handData is None:
        return None

    gesture = handData["gesture"]
    confidence = handData["confidence"]

    filtered = confidence_filter.filter(
        gesture,
        confidence
    )

    stable = prediction_buffer.update(filtered)

    verified = fusion.fuse(
        gesture,
        stable,
        confidence
    )

    # Final gesture stabilization
    stable_gesture = stabilizer.update(verified)

    action = GESTURE_ACTIONS.get(
        stable_gesture
    )

    handData["gesture"] = stable_gesture

    return queue.update(action)


def apply_landmark_filters(allHands, handTypes):

    filtered_hands = []

    left_seen = False
    right_seen = False

    for hand, handType in zip(allHands, handTypes):

        if handType == "Left":
            filtered = left_filter.smooth(hand)
            left_seen = True

        elif handType == "Right":
            filtered = right_filter.smooth(hand)
            right_seen = True

        else:
            filtered = hand

        filtered_hands.append(filtered)

    # Reset filters when the corresponding hand disappears
    if not left_seen:
        left_filter.reset()

    if not right_seen:
        right_filter.reset()

    return filtered_hands

profiler = PerformanceProfiler()

smoothX = 0
smoothY = 0
glow_phase = 0
handAngle = 0
orbit_angle = 0

previousGesture = "UNKNOWN"
confidence = 0.0
gesture_state = GestureState.NONE


tips = [4, 8, 12, 16, 20]
points = [0, 5, 9, 13, 17]

current_action = None
verified_gesture = "UNKNOWN"

ai_prediction = "UNKNOWN"
filtered_prediction = "UNKNOWN"
stable_prediction = "UNKNOWN"
ai_confidence = 0.0

ENABLE_ADVANCED_EFFECTS = True
DEBUG_PROFILER =  True

while True:

    success, frame = camera.read()
    dt = frame_timer.delta()
    profiler.start()
    energy.regenerate()
    

    if not success:
        break

    frame = cv2.flip(frame, 1)

    # Detect hand
    frame = detector.findHands(frame)

    if DEBUG_PROFILER:
        profiler.check("MediaPipe Only")
    # Get landmark positions
    allHands, handTypes = detector.findPosition(frame)

    if DEBUG_PROFILER:
        profiler.check("findPosition")

    # ==============================
    # Landmark Smoothing
    # ==============================

    allHands = apply_landmark_filters(
        allHands,
        handTypes
    )

    result = gesture_pipeline.process(
        allHands,
        handTypes
    )
    if DEBUG_PROFILER:
        profiler.check("Gesture Pipeline")

    leftData = result["left"]
    rightData = result["right"]

    left_gesture = leftData["gesture"]
    left_conf = leftData["confidence"]

    right_gesture = rightData["gesture"]
    right_conf = rightData["confidence"]

    leftHand = leftData["hand"]
    rightHand = rightData["hand"]

    left_gesture = leftData["gesture"]
    right_gesture = rightData["gesture"]

    left_state = leftData["state"]
    right_state = rightData["state"]

    power = result["two_hand_power"]
    
    # ==========================
    # Two-Hand Powers
    # ==========================

    if DEBUG_PROFILER:
        profiler.check("Hand Detection")
    
    if leftHand is not None and rightHand is not None:
        currentHand = "LEFT + RIGHT"

    elif leftHand is not None:
        currentHand = "LEFT"

    elif rightHand is not None:
        currentHand = "RIGHT"

    else:
        currentHand = "NONE"

    

    leftHandData = left_processor.process(leftHand)

    rightHandData = right_processor.process(rightHand)
    if DEBUG_PROFILER:
        profiler.check("Hand Processors")

    # Merge GesturePipeline + HandProcessor data

    if leftData is not None and leftHandData is not None:
        leftData = {**leftData, **leftHandData}

    if rightData is not None and rightHandData is not None:
        rightData = {**rightData, **rightHandData}

        # cv2.putText(
        #     frame,
        #     f"Gesture : {rightData['gesture']}",
        #     (20, 40),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     0.7,
        #     (0, 255, 0),
        #     2
        # )

    left_ai = leftData["gesture"]
    left_conf = leftData["confidence"]

    right_ai = rightData["gesture"]
    right_conf = rightData["confidence"]

    if rightHand is not None:
        collector.update(rightHand)

    left_action = process_hand(
        leftData,
        left_power_queue,
        left_prediction_buffer,
        left_confidence_filter,
        left_stabilizer
    )

    right_action = process_hand(
        rightData,
        right_power_queue,
        right_prediction_buffer,
        right_confidence_filter,
        right_stabilizer
    )     

    # Use the hand that is actually detected
    if rightHand is not None and right_action is not None:
        current_action = right_action

    elif leftHand is not None and left_action is not None:
        current_action = left_action

    else:
        current_action = None

    power_hud.draw(
        frame,
        current_action
    )

    if rightHandData is not None:
        handData = rightData

    elif leftHandData is not None:
        handData = leftData

    else:
        handData = None

    if handData:

        trail.update(
            frame,
            (
                handData["smoothX"],
                handData["smoothY"]
            )
        )

        gesture_flash.draw(
            frame,
            (
                handData["smoothX"],
                handData["smoothY"]
            )
        )

    # ---------- Add Here ----------
    hand_status = (
        "Detected"
        if rightHand is not None and len(rightHand) >= 21
        else "Not Detected"
    )

    tracking = (
        "ON"
        if rightHand is not None and len(rightHand) >= 21
        else "OFF"
    )

    DEBUG_AI = False

    if DEBUG_AI:

        cv2.putText(
            frame,
            f"Recording : {'ON' if collector.recording else 'OFF'}",
            (20,300),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0) if collector.recording else (0,0,255),
            2
        )

        cv2.putText(
            frame,
            f"Label : {collector.current_label or 'NONE'}",
            (20,330),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Samples : {collector.total_samples}",
            (20,360),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )

        cv2.putText(
            frame,
            f"Raw : {ai_prediction}",
            (20,390),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Confidence : {ai_confidence:.2f}",
            (20,420),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2
        )

        cv2.putText(
            frame,
            f"Filtered : {filtered_prediction}",
            (20,450),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            f"Stable : {stable_prediction}",
            (20,480),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255,255,255),
            2
        )
    # Draw fingertips and palm center
          
 
    if handData is None:

        left_prediction_buffer.clear()
        right_prediction_buffer.clear()

        left_stabilizer.reset()
        right_stabilizer.reset()

        stable_prediction = "UNKNOWN"

        previousGesture = "UNKNOWN"

        gesture_pipeline.reset()

        target_lock.reset()

        left_power_queue.reset()
        right_power_queue.reset()
        left_confidence_filter.reset()
        right_confidence_filter.reset()

        # Stop any looping sounds (e.g. portal) once tracking is lost
        sound_manager.stop_loop()
       

   
    # Particle systems
    if DEBUG_PROFILER:
        profiler.check("Before Power Pipeline")
    # Debug Disabled
    pass 

    if handData is not None:

        power_pipeline.update(
            frame,
            rightData if rightHandData is not None else None,
            leftData if leftHandData is not None else None,
            power
        )

        physics_engine.update(dt)

        h, w = frame.shape[:2]
        physics_engine.bounce_screen(w, h)

        if ENABLE_ADVANCED_EFFECTS:
            animation_pipeline.update(
                frame,
                dt
            )
    if DEBUG_PROFILER:
        profiler.check("Animations")

    
    # FPS
    fps = calculate_fps()

    if ENABLE_ADVANCED_EFFECTS:
        frame = animation_pipeline.post_process(frame)

    render_pipeline.render(
        frame,
        handData,
        energy.get(),
        fps
    )

    status_bar.draw(
        frame,
        fps,
        energy.get(),
        current_action
    )

    if DEBUG_PROFILER:
        profiler.check("Rendering")

    

    cv2.imshow(
        "AI Hand Gesture Superpower",
        frame
    )

    key = cv2.waitKey(1) & 0xFF


    # ---------------------------------
    # Dataset Collection
    # ---------------------------------

    if rightHand is not None and len(rightHand) >= 21:

        if key == ord("1"):
            collector.start_recording("OPEN_HAND")

        elif key == ord("2"):
            collector.start_recording("FIST")

        elif key == ord("3"):
            collector.start_recording("THUMBS_UP")

        elif key == ord("4"):
            collector.start_recording("PEACE")

        elif key == ord("5"):
            collector.start_recording("PINCH")

        elif key == ord("6"):
            collector.start_recording("ROCK")

        elif key == ord("7"):
            collector.start_recording("ONE_FINGER")

        elif key == ord("8"):
            collector.start_recording("SPIDER")

        elif key == ord("0"):
            collector.stop_recording()

    # ---------------------------------
    # Sound Volume Control (Step 94)
    # ---------------------------------

    elif key == ord("+"):
        sound_manager.set_volume(0.9)

    elif key == ord("-"):
        sound_manager.set_volume(0.3)

    # Quit

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
