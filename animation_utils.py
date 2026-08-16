import cv2
import math
import random

from numpy import angle


class AnimationUtils:

    @staticmethod
    def glow_circle(frame, center, radius, color, thickness=-1):
        cv2.circle(
            frame,
            center,
            int(radius),
            color,
            thickness,
            lineType=cv2.LINE_AA
        )

    @staticmethod
    def ring(frame, center, radius, color, thickness=2):
        cv2.circle(
            frame,
            center,
            int(radius),
            color,
            thickness,
            lineType=cv2.LINE_AA
        )

    @staticmethod
    def beam(frame, start, end, color, thickness):

        cv2.line(
            frame,
            start,
            end,
            color,
            thickness,
            lineType=cv2.LINE_AA
        )

        if thickness >= 5:

            cv2.line(
                frame,
                start,
                end,
                (255,255,255),
                1,
                lineType=cv2.LINE_AA
            )

    @staticmethod
    def pulse(value, amplitude):
        return amplitude * math.sin(value)

    @staticmethod
    def orbit(center, radius, angle):
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        return (
            int(center[0] + radius * cos_angle),
            int(center[1] + radius * sin_angle)
        )
    
    @staticmethod
    def sparkle(frame, center, color, radius=3):
        cv2.circle(
            frame,
            center,
            radius,
            color,
            -1,
            lineType=cv2.LINE_AA
        )


    @staticmethod
    def cross(frame, center, size, color):
        x, y = center

        cv2.line(
            frame,
            (x - size, y),
            (x + size, y),
            color,
            1,
            lineType=cv2.LINE_AA
        )

        cv2.line(
            frame,
            (x, y - size),
            (x, y + size),
            color,
            1,
            lineType=cv2.LINE_AA
        )


    @staticmethod
    def random_point(center, radius):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, radius)

        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        return (
            int(center[0] + distance * cos_angle),
            int(center[1] + distance * sin_angle)
        )
    
    @staticmethod
    def arc(frame, center, radius, start_angle, end_angle, color, thickness=2):
        cv2.ellipse(
            frame,
            center,
            (int(radius), int(radius)),
            0,
            start_angle,
            end_angle,
            color,
            thickness,
            lineType=cv2.LINE_AA
        )

    @staticmethod
    def energy_ball(frame, center, radius, outer_color, middle_color, core_color):

        # Outer glow
        AnimationUtils.glow_circle(
            frame,
            center,
            radius + 10,
            outer_color
        )

        # Middle layer
        AnimationUtils.glow_circle(
            frame,
            center,
            radius,
            middle_color
        )

        # Bright core
        AnimationUtils.glow_circle(
            frame,
            center,
            max(radius - 6, 1),
            core_color
        )

    @staticmethod
    def impact_flash(frame, center, radius, color):

        AnimationUtils.glow_circle(
            frame,
            center,
            radius + 15,
            color
        )

        AnimationUtils.glow_circle(
            frame,
            center,
            radius,
            (255, 255, 255)
        )    
    @staticmethod
    def smoke_cloud(frame, center, radius):

        AnimationUtils.glow_circle(
            frame,
            center,
            radius,
            (70, 70, 70)
        )

        AnimationUtils.glow_circle(
            frame,
            center,
            max(radius // 2, 1),
            (120, 120, 120)
        )

    @staticmethod
    def particle_glow(frame, center, radius, outer_color, inner_color):

        AnimationUtils.glow_circle(
            frame,
            center,
            radius,
            outer_color
        )

        AnimationUtils.glow_circle(
            frame,
            center,
            max(radius // 2, 1),
            inner_color
        )

    @staticmethod
    def electric_arc(frame, start, end):

        # Outer glow
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 180, 0),
            8
        )

        # Main bolt
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 255, 0),
            3
        )

        # Bright core
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 255, 255),
            1
        )

    @staticmethod
    def frost_beam(frame, start, end):

        # Blue glow
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 180, 100),
            10
        )

        # Ice beam
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 255, 180),
            4
        )

        # White core
        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 255, 255),
            1
        )

    @staticmethod
    def web_pattern(frame, center, radius):

        x, y = center

        # Center
        AnimationUtils.ring(
            frame,
            center,
            8,
            (255, 255, 255),
            -1
        )

        AnimationUtils.ring(
            frame,
            center,
            18,
            (220, 220, 220),
            2
        )

        # Radial lines
        for angle in range(0, 360, 45):

            rad = math.radians(angle)

            cos_angle = math.cos(rad)
            sin_angle = math.sin(rad)

            x2 = int(x + radius * cos_angle)
            y2 = int(y + radius * sin_angle)

            AnimationUtils.beam(
                frame,
                center,
                (x2, y2),
                (220, 220, 220),
                1
            )

        # Circular rings
        for r in range(20, radius, 20):

            AnimationUtils.ring(
                frame,
                center,
                r,
                (220, 220, 220),
                1
            )

    @staticmethod
    def web_strands(frame, center, radius):

        x, y = center

        for r in range(20, radius, 20):

            for angle in range(22, 360, 45):

                rad = math.radians(angle)

                cos_angle = math.cos(rad)
                sin_angle = math.sin(rad)

                x1 = int(x + r * cos_angle)
                y1 = int(y + r * sin_angle)

                x2 = int(x + (r + 20) * cos_angle)
                y2 = int(y + (r + 20) * sin_angle)

                AnimationUtils.beam(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (230, 230, 230),
                    1
                )

    @staticmethod
    def shield_ring(frame, center, radius, color):

        AnimationUtils.ring(
            frame,
            center,
            radius,
            color,
            2
        )

    @staticmethod
    def laser_beam(frame, start, end):

        AnimationUtils.beam(
            frame,
            start,
            end,
            (0, 0, 255),
            8
        )

        AnimationUtils.beam(
            frame,
            start,
            end,
            (0, 255, 255),
            4
        )

        AnimationUtils.beam(
            frame,
            start,
            end,
            (255, 255, 255),
            2
        )

    @staticmethod
    def energy_spokes(frame, center, radius, rotation, color):

        x, y = center

        for i in range(4):

            angle = math.radians(rotation + i * 45)

            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)

            px = int(x + radius * cos_angle)
            py = int(y + radius * sin_angle)

            AnimationUtils.beam(
                frame,
                (x, y),
                (px, py),
                color,
                1
            )                                        

    @staticmethod
    def rotating_nodes(frame, center, radius, rotation):

        x, y = center

        for i in range(4):

            angle = math.radians(rotation + i * 45)

            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)

            px = int(x + radius * cos_angle)
            py = int(y + radius * sin_angle)

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                8,
                (255, 255, 100)
            )

            AnimationUtils.glow_circle(
                frame,
                (px, py),
                4,
                (255, 255, 255)
            )

    @staticmethod
    def rotating_arcs(frame, center, radius, rotation):

        for i in range(2):

            start = rotation + i * 90
            end = start + 45

            AnimationUtils.arc(
                frame,
                center,
                radius,
                start,
                end,
                (255, 255, 255),
                2
            )

    @staticmethod
    def floating_particles(frame, particles):

        for p in particles:

            p.life -= 1
            p.angle += 0.1

            cos_angle = math.cos(p.angle)
            sin_angle = math.sin(p.angle)

            px = int(p.radius * cos_angle)
            py = int(p.radius * sin_angle)

            AnimationUtils.glow_circle(
                frame,
                (
                    int(p.center[0] + px),
                    int(p.center[1] + py)
                ),
                2,
                (255, 255, 255)
            )

    @staticmethod
    def shield_ripple(frame, center, radius):

        AnimationUtils.ring(
            frame,
            center,
            radius,
            (255, 255, 255),
            1
        )                        
    @staticmethod
    def dynamic_light(
        frame,
        center,
        radius,
        color,
        alpha=0.25
    ):
        """
        Draw soft dynamic lighting using alpha blending.
        """

        overlay = frame.copy()

        radius = int(radius)

        # Large soft glow
        cv2.circle(
            overlay,
            center,
            radius,
            color,
            -1,
            lineType=cv2.LINE_AA
        )
        inverse_alpha = 1.0 - alpha

        # Blend with original frame
        cv2.addWeighted(
            overlay,
            alpha,
            frame,
            inverse_alpha,
            0,
            frame
        )