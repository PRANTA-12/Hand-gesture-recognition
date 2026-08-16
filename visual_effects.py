import cv2


class VisualEffects:

    def __init__(self):
        pass

    def draw_finger_glow(
        self,
        frame,
        lmList,
        tips,
        orbit_angle
    ):

        finger_glow = frame.copy()

        for tip in tips:

            x = lmList[tip][1]
            y = lmList[tip][2]

            cv2.circle(
                finger_glow,
                (x, y),
                18,
                (255, 255, 0),
                -1
            )

        cv2.addWeighted(
            finger_glow,
            0.18,
            frame,
            0.82,
            0,
            frame
        )

        for tip in tips:

            x = lmList[tip][1]
            y = lmList[tip][2]

            cv2.circle(
                frame,
                (x, y),
                7,
                (255, 255, 255),
                -1,
                lineType=cv2.LINE_AA
            )

            cv2.circle(
                frame,
                (x, y),
                16,
                (255, 255, 255),
                -1,
                lineType=cv2.LINE_AA
            )

            cv2.circle(
                frame,
                (x, y),
                8,
                (255, 255, 0),
                -1,
                lineType=cv2.LINE_AA
            )

            cv2.ellipse(
                frame,
                (x, y),
                (12, 12),
                orbit_angle,
                0,
                270,
                (255, 255, 0),
                1,
                lineType=cv2.LINE_AA
            )

    def draw_palm_glow(
        self,
        frame,
        smoothX,
        smoothY,
        glow_radius
    ):

        glow = frame.copy()

        cv2.circle(
            glow,
            (smoothX, smoothY),
            glow_radius,
            (255, 255, 0),
            -1
        )

        cv2.addWeighted(
            glow,
            0.15,
            frame,
            0.85,
            0,
            frame
        ) 

    def draw_power_aura(
        self,
        frame,
        smoothX,
        smoothY,
        name
    ):

        power_aura = {
            "THUMBS_UP": (0, 140, 255),
            "ROCK": (255, 255, 0),
            "OPEN_HAND": (255, 255, 255),
            "TWO_FINGERS": (255, 180, 0),
            "SPIDER": (180, 180, 180),
            "ONE_FINGER": (255, 255, 0)
        }

        if name not in power_aura:
            return

        aura = frame.copy()

        cv2.circle(
            aura,
            (smoothX, smoothY),
            55,
            power_aura[name],
            -1
        )

        cv2.addWeighted(
            aura,
            0.08,
            frame,
            0.92,
            0,
            frame
        )

    def draw_orbit_rings(
        self,
        frame,
        smoothX,
        smoothY,
        orbit_angle
    ):

        import cv2
        import math

        for i in range(4):

            angle = math.radians(orbit_angle + i * 90)

            px = int(smoothX + 35 * math.cos(angle))
            py = int(smoothY + 35 * math.sin(angle))

            cv2.circle(
                frame,
                (px, py),
                3,
                (255, 255, 255),
                -1,
                lineType=cv2.LINE_AA
            )

    def draw_energy_lines(
        self,
        frame,
        lmList,
        tips,
        smoothX,
        smoothY
    ):

        import cv2

        for tip in tips:

            tipX = lmList[tip][1]
            tipY = lmList[tip][2]

            cv2.line(
                frame,
                (smoothX, smoothY),
                (tipX, tipY),
                (255,255,0),
                2,
                lineType=cv2.LINE_AA
            )

    def draw_power_lighting(
        self,
        frame,
        smoothX,
        smoothY,
        name
    ):

        import cv2

        power_light = {
            "THUMBS_UP": (0,140,255),
            "OPEN_HAND": (255,255,255),
            "ONE_FINGER": (255,255,0),
            "FIST": (255,0,0),
            "ROCK": (255,255,0),
            "TWO_FINGERS": (255,180,0),
            "SPIDER": (180,180,180)
        }

        if name not in power_light:
            return

        overlay = frame.copy()

        cv2.circle(
            overlay,
            (smoothX, smoothY),
            170,
            power_light[name],
            -1
        )

        cv2.addWeighted(
            overlay,
            0.05,
            frame,
            0.95,
            0,
            frame
        )

    def draw_vignette(self, frame):

        import cv2

        overlay = frame.copy()

        cv2.rectangle(
            overlay,
            (0, 0),
            (frame.shape[1], frame.shape[0]),
            (0, 0, 0),
            40
        )

        cv2.addWeighted(
            overlay,
            0.08,
            frame,
            0.92,
            0,
            frame
        )

        return frame                                   