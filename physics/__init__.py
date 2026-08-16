"""
Physics Engine Package

This package contains the reusable physics system for the
AI Hand Gesture Superpower Project.

Modules:
    vector2.py
    physics_body.py
    physics_engine.py
    collision_manager.py

Author: Pranta Pratap Ghosh
Project: AI Hand Gesture Superpower System
Version: 1.0
"""

from .vector2 import Vector2
from .physics_body import PhysicsBody
from .physics_engine import PhysicsEngine
from .collision_manager import CollisionManager

__all__ = [
    "Vector2",
    "PhysicsBody",
    "PhysicsEngine",
    "CollisionManager",
]