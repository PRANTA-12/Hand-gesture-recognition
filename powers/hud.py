import cv2
import math

class HUD:

    def __init__(self):
        self.scan_y = 50
        self.glow_phase = 0
        self.rotation = 0
        self.radar_radius = 0

        self.current_power = "UNKNOWN"
        self.previous_power = "UNKNOWN"
        self.fade_alpha = 255
        self.fade_speed = 12

        # Notification
        self.notification = ""
        self.notification_timer = 0
        self.notification_x = -250
        self.notification_alpha = 0
        self.shine_x = 0

    def draw(self, frame, power_name, confidence, energy, fps):

        # ===============================
        # Iron Man HUD Background
        # ===============================

        x = 15
        y = 15
        w = 340
        h = 240

        # ===============================
        # HUD Colors
        # ===============================

        self.glow_phase += 3

        if self.glow_phase >= 360:
            self.glow_phase = 0

        glow_value = 170 + int(
            80 * math.sin(
                math.radians(self.glow_phase)
            )
        )
        # Now define colors
        CYAN = (255, 255, 0)
        HUD_CYAN = (255, glow_value, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        ORANGE = (0, 165, 255)
        RED = (0, 0, 255)
        DARK = (20, 25, 35)
        # ======================================
        # Glass Background
        # ======================================

        overlay = frame.copy()

        cv2.rectangle(
            overlay,
            (x, y),
            (x + w, y + h),
            (20, 25, 35),
            -1
        )

        cv2.addWeighted(
            overlay,
            0.20,
            frame,
            0.80,
            0,
            frame
        )

        # Decorative corner lines

        corner = 18

        # Top Left
        cv2.line(frame,(x,y),(x+corner,y),HUD_CYAN,2)
        cv2.line(frame,(x,y),(x,y+corner),HUD_CYAN,2)

        # Top Right
        cv2.line(frame,(x+w,y),(x+w-corner,y),HUD_CYAN,2)
        cv2.line(frame,(x+w,y),(x+w,y+corner),HUD_CYAN,2)

        # Bottom Left
        cv2.line(frame,(x,y+h),(x+corner,y+h),HUD_CYAN,2)
        cv2.line(frame,(x,y+h),(x,y+h-corner),HUD_CYAN,2)

        # Bottom Right
        cv2.line(frame,(x+w,y+h),(x+w-corner,y+h),HUD_CYAN,2)
        cv2.line(frame,(x+w,y+h),(x+w,y+h-corner),HUD_CYAN,2)


        # Title

        title_blue = 180 + int(75 * math.sin(math.radians(self.rotation * 2)))
        title_color = (0, 255, title_blue)

        cv2.putText(
            frame,
            "SUPER POWER HUD",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            title_color,
            2
        )

        cv2.putText(
            frame,
            "AI Hand Gesture Recognition",
            (20, 52),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.40,
            WHITE,
            1
        )
        
        # ===============================
        # Animated Scan Line
        # ===============================

        cv2.line(
            frame,
            (x + 10, self.scan_y),
            (x + w - 10, self.scan_y),
            CYAN,
            2
        )

        self.scan_y += 2

        if self.scan_y > y + h - 20:
            self.scan_y = y + 20


        # ======================================
        # Power Core
        # ======================================

        core_x = x + w - 55
        core_y = y + 45

        # Outer ring
        cv2.ellipse(
            frame,
            (core_x, core_y),
            (24, 24),
            self.rotation,
            0,
            300,
            HUD_CYAN,
            2,
            lineType=cv2.LINE_AA
        )

        cv2.ellipse(
            frame,
            (core_x, core_y),
            (18, 18),
            -self.rotation,
            180,
            360,
            WHITE,
            2,
            lineType=cv2.LINE_AA
        )

        # Inner ring
        cv2.circle(
        frame,
        (core_x, core_y),
        14,
        WHITE,
        1
        )

        # Core
        cv2.circle(
            frame,
            (core_x, core_y),
            5,
            GREEN,
            -1
        ) 

        self.rotation += 3

        if self.rotation >= 360:
            self.rotation = 0   

        # ===============================
        # Divider Lines
        # ===============================

        cv2.line(frame, (25, 45), (330, 45), CYAN, 1)

        cv2.line(frame, (25, 105), (330, 105), (80, 180, 255), 1)

        cv2.line(frame, (25, 155), (330, 155), (80, 180, 255), 1)

        cv2.line(frame, (25, 205), (330, 205), (80, 180, 255), 1)

        

        
        # ======================================
        # Gesture Section
        # ======================================

        cv2.putText(
            frame,
            "GESTURE",
            (30, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            CYAN,
            1
        )

        power_colors = {
            "THUMBS UP": (0,140,255),     # Fireball
            "ROCK": CYAN,          # Lightning
            "OPEN HAND": WHITE,   # Shield
            "TWO FINGERS": (255,180,0),   # Ice
            "SPIDER": (180,180,180),      # Spider Web
            "ONE FINGER": (0,255,255),    # Laser
            "UNKNOWN": (180,180,180)
        }

        power_color = power_colors.get(power_name, WHITE)

        if power_name != self.current_power:

            self.previous_power = self.current_power
            self.current_power = power_name

            self.fade_alpha = 0

            self.notification = f"{power_name} ACTIVATED"
            self.notification_timer = 60

            self.notification_x = -250
            self.notification_alpha = 0

        if  self.fade_alpha < 255:
            self.fade_alpha += self.fade_speed

        fade = self.fade_alpha / 255.0

        fade_color = (
            int(power_color[0] * fade),
            int(power_color[1] * fade),
            int(power_color[2] * fade)
        )

        cv2.putText(
            frame,
            f"POWER : {self.current_power}",
            (45, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            fade_color,
            2,
            lineType=cv2.LINE_AA
        )    


        # Power Status
        status = "READY" if energy > 20 else "LOW POWER"

        status_color = (
            GREEN
            if energy > 20
            else RED
        )

        # ======================================
        # Status Section
        # ======================================

        cv2.putText(
            frame,
            "STATUS",
            (30,145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            CYAN,
            1
        )

        cv2.putText(
            frame,
            status,
            (30,175),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            status_color,
            2
        ) 

        cv2.putText(
            frame,
            "ENERGY",
            (30,190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            CYAN,
            1
        )

        cv2.putText(
            frame,
            f"{energy} %",
            (240,190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            WHITE,
            2
        )

        # ======================================
        # Professional Energy Bar
        # ======================================

        bar_x = 25
        bar_y = 205

        bar_w = 260
        bar_h = 22

        # Background
        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + bar_w, bar_y + bar_h),
            (45,45,45),
            -1
        )

        # Border
        cv2.rectangle(
            frame,
            (bar_x, bar_y),
            (bar_x + bar_w, bar_y + bar_h),
            CYAN,
            2
        )

        fill = int((energy/100)*bar_w)

        # Dynamic color

        if energy > 60:
            color = GREEN

        elif energy > 30:
            color = (0,255,255)

        else:
            color = RED

        # Fill
        cv2.rectangle(
            frame,
            (bar_x+2,bar_y+2),
            (bar_x+fill-2,bar_y+bar_h-2),
            color,
            -1
        )

        cv2.putText(
            frame,
            f"CONFIDENCE : {confidence*100:.1f}%",
            (45, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255,255,255),
            1,
            lineType=cv2.LINE_AA
        )

        # ======================================
        # Animated Energy Glow
        # ======================================

        glow_strength = 180 + int(75 * math.sin(math.radians(self.rotation * 3)))

        glow_color = (
            glow_strength,
            glow_strength,
            glow_strength
        )

        cv2.rectangle(
            frame,
            (bar_x + 2, bar_y + 2),
            (bar_x + fill - 2, bar_y + 6),
            glow_color,
            -1
        )

        self.shine_x += 6

        if self.shine_x > bar_w:
            self.shine_x = 0

        cv2.line(
            frame,
            (bar_x + self.shine_x, bar_y + 2),
            (bar_x + self.shine_x - 12, bar_y + bar_h - 2),
            WHITE,
            2,
            lineType=cv2.LINE_AA
        )

        fps_color = GREEN if fps >= 30 else (0,0,255)

        # ======================================
        # HUD Notification
        # ======================================

        if self.notification_timer > 0:

            if self.notification_x < 40:
                self.notification_x += 12

            cv2.putText(
                frame,
                self.notification,
                (int(self.notification_x), 255),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.60,
                (255, 255, 255),
                2,
                lineType=cv2.LINE_AA
            )

            self.notification_timer -= 1

        