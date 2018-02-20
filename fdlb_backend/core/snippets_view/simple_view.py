from core.base_components import BaseView


class ScalarView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or 0


class MatrixView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or [[]]

    def __getitem__(self, position):
        m, n = position
        return self.value[m][n]

    def __setitem__(self, position, val):
        m, n = position
        self.value[m][n] = val


class LabelView(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or ''


class ButtonView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        on_submit = kwargs.get('on_submit', None)
        if on_submit:
            self.add_event('submit', on_submit)
