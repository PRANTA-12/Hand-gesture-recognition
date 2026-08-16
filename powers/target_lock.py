import cv2
import math


class TargetLock:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.locked = False
        self.frames = 0
        self.lock_frames = 20
        self.rotation = 0

    def update(self, position):
        self.x, self.y = position

        if not self.locked:
            self.frames += 1

            if self.frames >= self.lock_frames:
                self.locked = True

    def reset(self):
        self.locked = False
        self.frames = 0

    def draw(self, frame):

        if self.frames == 0:
            return

        if self.x == 0 and self.y == 0:
            return

        color = (0, 255, 255)
        if self.frames > 0:

            self.rotation += 5

            if self.rotation >= 360:
                self.rotation = 0

        if self.locked:
            color = (0, 0, 255)

        AnimationRadius = 25
        cv2.circle(
            frame,
            (self.x, self.y),
            45,
            (60, 180, 255),
            1
        )
        cv2.circle(
            frame,
            (self.x, self.y),
            55,
            (40, 120, 180),
            1
        )

        cv2.circle(
            frame,
            (self.x, self.y),
            65,
            (20, 80, 120),
            1
        )

        pulse = int(
            4 * math.sin(
                math.radians(self.rotation * 5)
            )
        )

        # cv2.circle(
        #     frame,
        #     (self.x, self.y),
        #      AnimationRadius + pulse,
        #     color,
        #     2
        # )

        cv2.ellipse(
            frame,
            (self.x, self.y),
            (AnimationRadius + 10, AnimationRadius + 10),
            self.rotation,
            0,
            220,
            color,
            2
        )

        cv2.ellipse(
            frame,
            (self.x, self.y),
            (AnimationRadius + 10, AnimationRadius + 10),
            self.rotation + 180,
            0,
            220,
            color,
            2
        )

        radius = 30

        angle = math.radians(self.rotation)

        x1 = int(self.x + radius * math.cos(angle))
        y1 = int(self.y + radius * math.sin(angle))

        x2 = int(self.x - radius * math.cos(angle))
        y2 = int(self.y - radius * math.sin(angle))

        # cv2.line(
        #     frame,
        #     (x1, y1),
        #     (x2, y2),
        #     color,
        #     2
        # )
        # Radar sweep
        scan_radius = 45

        scan_angle = math.radians(self.rotation)

        scanX = int(
            self.x + scan_radius * math.cos(scan_angle)
        )

        scanY = int(
            self.y + scan_radius * math.sin(scan_angle)
        )

        # cv2.line(
        #     frame,
        #     (self.x, self.y),
        #     (scanX, scanY),
        #     (0, 120, 255),
        #     3
        # )

        # cv2.line(
        #     frame,
        #     (self.x, self.y),
        #     (scanX, scanY),
        #     (255, 255, 255),
        #     1
        # )

        size = 35 + int(
            2 * math.sin(
                math.radians(self.rotation * 4)
            )
        )
        # Top Left
        cv2.line(frame,
                (self.x-size, self.y-size),
                (self.x-size+12, self.y-size),
                color, 2)

        cv2.line(frame,
                (self.x-size, self.y-size),
                (self.x-size, self.y-size+12),
                color, 2)

        # Top Right
        cv2.line(frame,
                (self.x+size, self.y-size),
                (self.x+size-12, self.y-size),
                color, 2)

        cv2.line(frame,
                (self.x+size, self.y-size),
                (self.x+size, self.y-size+12),
                color, 2)

        # Bottom Left
        cv2.line(frame,
                (self.x-size, self.y+size),
                (self.x-size+12, self.y+size),
                color, 2)

        cv2.line(frame,
                (self.x-size, self.y+size),
                (self.x-size, self.y+size-12),
                color, 2)

        # Bottom Right
        cv2.line(frame,
                (self.x+size, self.y+size),
                (self.x+size-12, self.y+size),
                color, 2)

        cv2.line(frame,
                (self.x+size, self.y+size),
                (self.x+size, self.y+size-12),
                color, 2)

        cv2.line(frame,
                 (self.x - 15, self.y),
                 (self.x + 15, self.y),
                 color, 2)

        cv2.line(frame,
                 (self.x, self.y - 15),
                 (self.x, self.y + 15),
                 color, 2)
        
        # cv2.circle(
        #     frame,
        #     (self.x, self.y),
        #     4,
        #     color,
        #     -1
        # )
        
        progress = min(
            self.frames * 100 // self.lock_frames,
            100
        )

        bar_width = 60
        filled = bar_width * progress // 100

        cv2.putText(
            frame,
            f"{progress}%",
            (self.x - 18, self.y + 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2
        )
        cv2.putText(
            frame,
            "TARGET",
            (self.x - 28, self.y - 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (255, 255, 255),
            1
        )

        # Progress Bar Background
        cv2.rectangle(
            frame,
            (self.x - 30, self.y + 62),
            (self.x + 30, self.y + 68),
            (80, 80, 80),
            1
        )

        # Filled Progress
        cv2.rectangle(
            frame,
            (self.x - 30, self.y + 62),
            (self.x - 30 + filled, self.y + 68),
            color,
            -1
        )

        if self.locked:

            pulse = int(5 * math.sin(math.radians(self.rotation * 6)))
            
            cv2.putText(
                frame,
                "LOCKED",
                (self.x - 35, self.y - 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )
            cv2.circle(
                frame,
                (self.x, self.y),
                30 + pulse,
                (0, 0, 255),
                2
            )
            
        for i in range(4):

            a = math.radians(self.rotation + i * 90)

            px = int(self.x + 40 * math.cos(a))
            py = int(self.y + 40 * math.sin(a))

            dot_radius = 3 + int(
                abs(math.sin(math.radians(self.rotation * 6)))
            )

            cv2.circle(
                frame,
                (px, py),
                dot_radius,
                color,
                -1
            )
        for i in range(8):

            angle = math.radians(self.rotation * 2 + i * 45)

            px = int(self.x + 65 * math.cos(angle))
            py = int(self.y + 65 * math.sin(angle))

            cv2.circle(
                frame,
                (px, py),
                2,
                (255, 255, 0),
                -1
            )      