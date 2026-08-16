import math
import random
import cv2

from animation_utils import AnimationUtils


class LightningRenderer:

    def __init__(self):

        self.time = 0.0

    # ---------------------------------
    # Reset
    # ---------------------------------

    def reset(self):

        self.time = 0.0

    # ---------------------------------
    # Update
    # ---------------------------------

    def update(self, dt):

        self.time += dt * 15

    # ---------------------------------
    # Draw
    # ---------------------------------

    def draw(
        self,
        frame,
        start,
        end,
        intensity=1.0
    ):

        if intensity <= 0:
            return

        x1, y1 = start
        x2, y2 = end

        # ---------------------------------
        # Create Lightning Points
        # ---------------------------------

        points = [(x1, y1)]

        segments = 12

        for i in range(1, segments):

            t = i / segments

            px = x1 + (x2 - x1) * t
            py = y1 + (y2 - y1) * t

            base_offset = random.randint(-12, 12)

            wave = math.sin(self.time + i) * 8

            offset = int(base_offset + wave)

            dx = x2 - x1
            dy = y2 - y1

            length = math.hypot(dx, dy)

            if length != 0:

                nx = -dy / length
                ny = dx / length

                px += nx * offset
                py += ny * offset

            points.append((int(px), int(py)))

        points.append((x2, y2))

        # ---------------------------------
        # Multi Layer Glow + Beam Pulse
        # ---------------------------------

        pulse = (
            1.0 +
            0.18 * math.sin(self.time * 2.5)
        )

        outer_width = max(
            8,
            int(12 * pulse)
        )

        middle_width = max(
            5,
            int(8 * pulse)
        )

        inner_width = max(
            3,
            int(5 * pulse)
        )

        core_width = max(
            1,
            int(2 * pulse)
        )

        for i in range(len(points) - 1):

            # ---------------------------------
            # Outer Glow
            # ---------------------------------

            cv2.line(
                frame,
                points[i],
                points[i + 1],
                (80, 120, 255),
                outer_width,
                cv2.LINE_AA
            )

            # ---------------------------------
            # Middle Glow
            # ---------------------------------

            cv2.line(
                frame,
                points[i],
                points[i + 1],
                (150, 200, 255),
                middle_width,
                cv2.LINE_AA
            )

            # ---------------------------------
            # Inner Glow
            # ---------------------------------

            cv2.line(
                frame,
                points[i],
                points[i + 1],
                (220, 240, 255),
                inner_width,
                cv2.LINE_AA
            )

            # ---------------------------------
            # White Core
            # ---------------------------------

            cv2.line(
                frame,
                points[i],
                points[i + 1],
                (255, 255, 255),
                core_width,
                cv2.LINE_AA
            )

        # ---------------------------------
        # Secondary Branches
        # ---------------------------------   
        for i in range(2, len(points) - 2, 2):

            if random.random() < 0.25:

                bx, by = points[i]

                branch_angle = random.uniform(
                    0,
                    math.pi * 2
                )

                branch_length = random.randint(
                    20,
                    45
                )

                end_x = int(
                    bx + math.cos(branch_angle) * branch_length
                )

                end_y = int(
                    by + math.sin(branch_angle) * branch_length
                )

                # Glow branch
                cv2.line(
                    frame,
                    (bx, by),
                    (end_x, end_y),
                    (255, 220, 120),
                    max(3, int(5 * pulse)),
                    cv2.LINE_AA
                )

                # White core
                cv2.line(
                    frame,
                    (bx, by),
                    (end_x, end_y),
                    (255, 255, 255),
                    max(1, int(2 * pulse)),
                    cv2.LINE_AA
                )
        
        # ---------------------------------
        # Main Lightning
        # ---------------------------------

        for i in range(len(points) - 1):

            cv2.line(
                frame,
                points[i],
                points[i + 1],
                (255, 255, 255),
                core_width,
                cv2.LINE_AA
            )
        # ---------------------------------
        # Beam Sparks
        # ---------------------------------

        for i in range(len(points) - 1):

            if random.random() < 0.25:

                x1s, y1s = points[i]
                x2s, y2s = points[i + 1]

                t = random.random()

                sx = int(x1s + (x2s - x1s) * t)
                sy = int(y1s + (y2s - y1s) * t)

                AnimationUtils.glow_circle(
                    frame,
                    (sx, sy),
                    random.randint(2, 4),
                    random.choice([
                        (255, 255, 255),
                        (180, 220, 255),
                        (0, 180, 255)
                    ])
                )
        # ---------------------------------
        # Energy Nodes
        # ---------------------------------

        for i, point in enumerate(points):

            if i % 2 != 0:
                continue

            AnimationUtils.glow_circle(
                frame,
                point,
                4,
                (255, 255, 255)
            )

            AnimationUtils.glow_circle(
                frame,
                point,
                7,
                (0, 180, 255)
            )

        # ---------------------------------
        # Charging Orb
        # ---------------------------------

        # Outer Energy Aura
        AnimationUtils.glow_circle(
            frame,
            (x1, y1),
            36,
            (0, 120, 255)
        )

        # Middle Aura
        AnimationUtils.glow_circle(
            frame,
            (x1, y1),
            26,
            (120, 220, 255)
        )

        # White Core
        AnimationUtils.glow_circle(
            frame,
            (x1, y1),
            16,
            (255, 255, 255)
        )

        # ---------------------------------
        # Orbiting Energy Particles
        # ---------------------------------

        for i in range(8):

            angle = self.time * 4 + i * (math.pi / 4)

            radius = 24

            px = int(
                x1 + math.cos(angle) * radius
            )

            py = int(
                y1 + math.sin(angle) * radius
            )

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                3,
                (255, 255, 255)
            )

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                6,
                (0, 180, 255)
            )
        # ---------------------------------
        # Random Electric Arcs
        # ---------------------------------

        for _ in range(4):

            start_angle = random.uniform(
                0,
                math.pi * 2
            )

            end_angle = (
            start_angle +
            random.uniform(-0.8, 0.8)
            )

            start_radius = random.randint(14, 20)
            end_radius = random.randint(22, 34)

            ax1 = int(
                x1 +
                math.cos(start_angle) *
                start_radius
            )

            ay1 = int(
                y1 +
                math.sin(start_angle) *
                start_radius
            )

            ax2 = int(
                x1 +
                math.cos(end_angle) *
                end_radius
            )

            ay2 = int(
                y1 +
                math.sin(end_angle) *
                end_radius
            )

            arc_points = [(ax1, ay1)]

            # Create jagged arc points
            for i in range(1, 4):

                t = i / 4

                px = ax1 + (ax2 - ax1) * t
                py = ay1 + (ay2 - ay1) * t

                px += random.randint(-5, 5)
                py += random.randint(-5, 5)

                arc_points.append(
                    (int(px), int(py))
                )

            # Add final point AFTER the loop
            arc_points.append(
                (ax2, ay2)
            )

            # ---------------------------------
            # Arc Glow
            # ---------------------------------

            for j in range(len(arc_points) - 1):

                cv2.line(
                    frame,
                    arc_points[j],
                    arc_points[j + 1],
                    (80, 180, 255),
                    max(3, int(5 * pulse)),
                    cv2.LINE_AA
                )

            # ---------------------------------
            # Arc Core
            # ---------------------------------

            for j in range(len(arc_points) - 1):

                cv2.line(
                    frame,
                    arc_points[j],
                    arc_points[j + 1],
                    (255, 255, 255),
                    max(1, int(2 * pulse)),
                    cv2.LINE_AA
                )    

        # ---------------------------------
        # Impact Flash
        # ---------------------------------

        # Outer Electric Glow
        AnimationUtils.glow_circle(
            frame,
            (x2, y2),
            40,
            (0, 120, 255)
        )

        # Blue Glow
        AnimationUtils.glow_circle(
            frame,
            (x2, y2),
            28,
            (120, 220, 255)
        )

        # White Flash
        AnimationUtils.glow_circle(
            frame,
            (x2, y2),
            16,
            (255, 255, 255)
        )

        # Electric Ring
        cv2.circle(
            frame,
            (x2, y2),
            32,
            (180, 255, 255),
            2,
            cv2.LINE_AA
        )
        # ---------------------------------
        # Impact Sparks
        # ---------------------------------

        for _ in range(8):

            angle = random.uniform(0, math.pi * 2)

            length = random.randint(8, 22)

            ex = int(x2 + math.cos(angle) * length)
            ey = int(y2 + math.sin(angle) * length)

            cv2.line(
                frame,
                (x2, y2),
                (ex, ey),
                random.choice([
                    (255,255,255),
                    (180,220,255),
                    (0,180,255)
                ]),
                max(1, int(2 * pulse)),
                cv2.LINE_AA
            )