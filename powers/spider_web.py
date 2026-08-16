from continuous_animation import ContinuousAnimation
from animation_utils import AnimationUtils
from animation_config import AnimationConfig
from trail_manager import TrailManager
import cv2
import math
import random


class SpiderWeb(ContinuousAnimation):

    def __init__(self):
        super().__init__()

        self.angle = 0

        self.x = 0
        self.y = 0

        self.speed = AnimationConfig.FIREBALL_SPEED

        self.vx = 0
        self.vy = 0
        self.trail = TrailManager(AnimationConfig.SPIDER_TRAIL)
        self.expand = 10
        self.distance = 0
        self.max_distance = AnimationConfig.SPIDER_MAX_DISTANCE
        self.hit = False
        self.dust = []

    def start(self, position, angle):
        super().start(position)
        self.angle = angle

        self.x = position[0]
        self.y = position[1]

        self.vx = self.speed * math.cos(angle)
        self.vy = self.speed * math.sin(angle)
        self.trail.clear()
        self.expand = 10
        self.distance = 0
        self.hit = False
        self.dust.clear()

    def move(self, position):
        self.position = position    

    def update(self, frame, dt):

        if not self.active:
            return

        self.x += self.vx * dt * 60
        self.y += self.vy * dt * 60
        self.distance += self.speed * dt * 60
       
        if self.distance >= self.max_distance and not self.hit:

            self.vx = 0
            self.vy = 0
            self.hit = True

            # Create dust once
            for _ in range(15):

                self.dust.append({
                    "x": self.x,
                    "y": self.y,
                    "dx": math.cos(random.uniform(0, 2 * math.pi)) * 2,
                    "dy": math.sin(random.uniform(0, 2 * math.pi)) * 2,
                    "life": 20
                })

            

         # Update dust
        for d in self.dust[:]:

            d["x"] += d["dx"] * dt * 60
            d["y"] += d["dy"] * dt * 60
            d["life"] -= 1

            AnimationUtils.glow_circle(
                frame,
                (int(d["x"]), int(d["y"])),
                2,
                (200, 200, 200)
            )

            if d["life"] <= 0:
                self.dust.remove(d)        

    
            
        x = int(self.x)
        y = int(self.y)

        self.trail.add((x, y))

        self.trail.draw(
            frame,
            outer_color=(180, 180, 180),
            inner_color=(255, 255, 255)
        )

        if self.hit and self.expand < 300:
            self.expand += 180 * dt

        radius = int(self.expand)

        if self.hit:
            AnimationUtils.ring(
                frame,
                (x, y),
                radius,
                (200, 200, 200),
                1
            )    

            # Web glow
            AnimationUtils.ring(
                frame,
                (x, y),
                radius + 8,
                (180, 180, 180),
                2
            )

            
            AnimationUtils.web_pattern(
                frame,
                (x, y),
                radius
            )

            AnimationUtils.web_strands(
                frame,
                (x, y),
                radius
            )    

    def stop(self):

        self.active = False

        self.trail.clear()
        self.dust.clear()

        self.hit = False
        self.expand = 10
        self.distance = 0        