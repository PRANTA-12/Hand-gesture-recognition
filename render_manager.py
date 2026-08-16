class RenderManager:

    def __init__(self):
        self.render_items = []

        self.animation_manager = None

    def add(self, priority, callback, *args, **kwargs):
        """
        Register a drawing function.

        priority:
            Lower number = drawn first
            Higher number = drawn later (on top)
        """
        self.render_items.append(
            (priority, callback, args, kwargs)
        )

    def render(self):
        if not self.render_items:
            return
        self.render_items.sort(key=lambda item: item[0])

        for _, callback, args, kwargs in self.render_items:
            callback(*args, **kwargs)

        self.render_items.clear()