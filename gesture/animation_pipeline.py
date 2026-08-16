class AnimationPipeline:

    def __init__(
        self,
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
    ):

        self.performance_monitor = performance_monitor

        self.particle_engine = particle_engine
        self.advanced_particles = advanced_particles

        self.effect_manager = effect_manager
        self.animation_manager = animation_manager

        self.enemy = enemy
        self.target_lock = target_lock

        self.camera_shake = camera_shake
        self.camera_zoom = camera_zoom
        self.motion_blur = motion_blur
        self.screen_flash = screen_flash

    # -----------------------------------
    # Update Animations
    # -----------------------------------

    def update(
        self,
        frame,
        dt
    ):

        self.performance_monitor.update()
        self.camera_shake.update(dt)

        self.camera_zoom.update()

        if self.particle_engine.particles:
            self.particle_engine.update(frame)

        if self.advanced_particles.particles:
            self.advanced_particles.update(frame)



        if self.effect_manager.effects:

            self.effect_manager.update(
                frame,
                dt
            )

        if self.animation_manager.animations:

            self.animation_manager.update(
                frame,
                dt
            )

        if self.enemy is not None:
            self.enemy.draw(frame)

        # if self.target_lock.locked:
        #     self.target_lock.draw(frame)

    # -----------------------------------
    # Post Processing
    # -----------------------------------

    def post_process(
        self,
        frame
    ):

        if self.camera_shake.active:
            frame = self.camera_shake.apply(frame)

        if self.camera_zoom.active:
            frame = self.camera_zoom.apply(frame)

        if self.motion_blur.active:
            frame = self.motion_blur.apply(frame)

        if self.screen_flash.active:
            self.screen_flash.update(frame)

        return frame

    # -----------------------------------
    # Reset
    # -----------------------------------

    def reset(self):

        self.target_lock.reset()