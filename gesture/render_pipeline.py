import cv2


class RenderPipeline:

    def __init__(
        self,
        render_manager,
        hud,
        visual_effects,
        performance_monitor
    ):

        self.render_manager = render_manager
        self.hud = hud
        self.visual_effects = visual_effects
        self.performance_monitor = performance_monitor

    # ---------------------------------
    # Render Everything
    # ---------------------------------

    def render(
        self,
        frame,
        handData,
        energy,
        fps
    ):
        
        if handData:

            gesture = handData["gesture"]

            confidence = handData["confidence"]

            smoothX = handData["smoothX"]

            smoothY = handData["smoothY"]

        else:

            gesture = "UNKNOWN"

            confidence = 0.0

            smoothX = 0

            smoothY = 0
        # -----------------------------
        # HUD
        # -----------------------------

        self.render_manager.add(

            100,

            self.hud.draw,

            frame,

            gesture,

            confidence,

            energy,

            fps

        )

        # -----------------------------
        # Dynamic Lighting
        # -----------------------------

        self.render_manager.add(

            200,

            self.visual_effects.draw_power_lighting,

            frame,

            smoothX,

            smoothY,

            gesture

        )
        # -----------------------------
        # Two-Hand Animations
        # -----------------------------

        for animation in self.render_manager.animation_manager.animations.values():

            if hasattr(animation, "draw"):

                self.render_manager.add(

                    250,

                    animation.draw,

                    frame

                )

        # -----------------------------
        # Cinematic Vignette
        # -----------------------------

        self.render_manager.add(

            300,

            self.visual_effects.draw_vignette,

            frame

        )

        # -----------------------------
        # FPS Counter
        # -----------------------------

        cv2.putText(

            frame,

            f"Real FPS : {self.performance_monitor.get_fps()}",

            (20, frame.shape[0] - 20),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (0, 255, 0),

            2

        )

        # -----------------------------
        # Execute Render Queue
        # -----------------------------

        self.render_manager.render()