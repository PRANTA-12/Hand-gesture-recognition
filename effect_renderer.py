from animation_utils import AnimationUtils
from effect_presets import EffectPresets


class EffectRenderer:

    @staticmethod
    def fireball(frame, center, radius):
        p = EffectPresets.FIREBALL

        AnimationUtils.energy_ball(
            frame,
            center,
            radius,
            p["outer"],
            p["middle"],
            p["core"]
        )

    @staticmethod
    def lightning_charge(frame, center, radius):
        p = EffectPresets.LIGHTNING

        AnimationUtils.energy_ball(
            frame,
            center,
            radius,
            p["outer"],
            p["middle"],
            p["core"]
        )

    @staticmethod
    def ice_core(frame, center, radius):
        p = EffectPresets.ICE

        AnimationUtils.energy_ball(
            frame,
            center,
            radius,
            p["outer"],
            p["middle"],
            p["core"]
        )

    @staticmethod
    def spider_web(frame, center, radius):
        p = EffectPresets.SPIDER

        AnimationUtils.energy_ball(
            frame,
            center,
            radius,
            p["outer"],
            p["middle"],
            p["core"]
        )    