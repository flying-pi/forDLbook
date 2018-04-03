from core.base_components import BaseView


class DrawableCanvas(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or ' '

