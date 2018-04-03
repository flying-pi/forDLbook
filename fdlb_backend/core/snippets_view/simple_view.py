from core.base_components import BaseView


class ScalarView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or 0

    def on_value_set(self, v):
        try:
            return float(v)
        except Exception:
            return v


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

    def on_value_set(self, v):
        return [[float(cell) for cell in row] for row in v]


class LabelView(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or ''


class ButtonView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        on_submit = kwargs.get('on_submit', None)
        redirect_to = kwargs.get('redirect_to', None)
        text = kwargs.get('text', None)
        self.value = self.value or {
            'redirect_to': redirect_to,
            'text': text,
        }
        if on_submit:
            self.add_event('submit', on_submit)


class SelectView(BaseView):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        placeholder = kwargs.get('placeholder')
        selected = kwargs.get('selected')
        options = kwargs.get('options', [])
        self.value = self.value or {'selected': selected, 'options': options, 'placeholder': placeholder}

    def add_item(self, marker, label):
        self.value['options'].append({
            'marker': marker,
            'label': label
        })

    def selected(self):
        return self.value['options'][self.value['selected']]


class UploadFile(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or ''
        on_upload = kwargs.get('on_upload', None)
        if on_upload:
            self.add_event('upload', on_upload)


class Image(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.value = self.value or ''

