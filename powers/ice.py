from continuous_animation import ContinuousAnimation
from animation_utils import AnimationUtils
from animation_config import AnimationConfig
from effect_renderer import EffectRenderer
import cv2
import random
import math


class Ice(ContinuousAnimation):

    def __init__(self):
        super().__init__()
        self.angle = 0
        self.crystals = []
        self.pulse = 0
        self.mist = []
        self.impact_crystals = []

    def start(self, position, angle=None):
        self.active = True
        self.position = position

        self.crystals.clear()
        self.mist.clear()
        self.impact_crystals.clear()

        if angle is not None:
            self.angle = angle

    def move(self, position):
        self.position = position        

    def update(self, frame, dt):

        if not self.active:
            return

        x, y = self.position
        # Create cold mist
        for _ in range(2):

            self.mist.append({
                "x": x,
                "y": y,
                "dx": random.uniform(-2, 2),
                "dy": random.uniform(-2, 2),
                "radius": random.randint(6, 12),
                "life": 25
            })

        self.pulse += 12 * dt

        # Create ice crystals
        for _ in range(3):

            self.crystals.append({
                "x": x,
                "y": y,
                "dx": random.uniform(-3, 3),
                "dy": random.uniform(-3, 3),
                "life": 25
            })
        
        if hasattr(self, "particles"):
            self.particles.emit(
                (x, y),
                color=(255, 255, 255),
                count=4,
                speed=1
            )

        # Draw ice crystals
        for c in self.crystals[:]:

            c["x"] += c["dx"] * dt * 60
            c["y"] += c["dy"] * dt * 60
            c["life"] -= 1

            AnimationUtils.glow_circle(
                frame,
                (int(c["x"]), int(c["y"])),
                3,
                (220, 255, 255)
            )

            if c["life"] <= 0:
                self.crystals.remove(c)

        # Draw cold mist
        for m in self.mist[:]:

            m["x"] += m["dx"] * dt * 60
            m["y"] += m["dy"] * dt * 60

            m["radius"] += 12 * dt
            m["life"] -= 1

            AnimationUtils.glow_circle(
                frame,
                (int(m["x"]), int(m["y"])),
                int(m["radius"]),
                (200, 240, 255)
            )

            if m["life"] <= 0:
                self.mist.remove(m)            

        for _ in range(40):

            distance = random.randint(20, AnimationConfig.ICE_BEAM_LENGTH)
            offset = random.randint(-40, 40)

            px = int(
                x
                + distance * math.cos(self.angle)
                - offset * math.sin(self.angle)
            )

            py = int(
                y
                + distance * math.sin(self.angle)
                + offset * math.cos(self.angle)
            ) 

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                random.randint(2, 5),
                (255, 255, 200)
            )

        

        endX = int(
            x + AnimationConfig.ICE_BEAM_LENGTH * math.cos(self.angle)
        )
        endY = int(
            y + AnimationConfig.ICE_BEAM_LENGTH * math.sin(self.angle)
        )

        # Create impact crystals
        if random.random() < 0.4:

            self.impact_crystals.append({
                "x": endX,
                "y": endY,
                "dx": random.uniform(-5, 5),
                "dy": random.uniform(-5, 5),
                "life": 20
            })

        # Snowflakes
        for _ in range(8):

            sx = random.randint(min(x, endX), max(x, endX))
            sy = random.randint(min(y, endY), max(y, endY))

            AnimationUtils.glow_circle(
                frame,
                (sx, sy),
                2,
                (255, 255, 255)
            )    

        AnimationUtils.frost_beam(
            frame,
            (x, y),
            (endX, endY)
        )

        # Frozen impact
        EffectRenderer.ice_core(
            frame,
            (endX, endY),
            18 + int(2 * math.sin(self.pulse))
        )

        # Draw impact crystals
        for ic in self.impact_crystals[:]:

            ic["x"] += ic["dx"] * dt * 60
            ic["y"] += ic["dy"] * dt * 60
            ic["life"] -= 1

            AnimationUtils.beam(
                frame,
                (int(ic["x"]), int(ic["y"])),
                (
                    int(ic["x"] + ic["dx"] * 2),
                    int(ic["y"] + ic["dy"] * 2)
                ),
                (220, 255, 255),
                2
            )

            if ic["life"] <= 0:
                self.impact_crystals.remove(ic)

    def stop(self):

        self.active = False

        self.crystals.clear()
        self.mist.clear()
        self.impact_crystals.clear()            