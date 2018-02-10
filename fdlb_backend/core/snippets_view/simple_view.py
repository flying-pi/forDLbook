from core.base_components import BaseView


class ScalarView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or 0


class MatrixView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        m = kwargs.get('m', 1)
        n = kwargs.get('n', 1)
        self.value = self.value or [[0 for j in range(n)] for i in range(m)]

    def __getitem__(self, position):
        m, n = position
        return self.value[m][n]

    def __setitem__(self, position, val):
        m, n = position
        self.value[m][n] = val
