import json
from abc import ABC, abstractmethod
from typing import List

from django.http import JsonResponse
from django.views import View as DjangoView


class BaseView(object):
    SUBMIT_EVENT_NAME = 'on_submit'
    """
    use function reference as event listener with next signature of the name: 
    on_{event_name}
    """

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__view_id = kwargs.get('view_id', None)
        self.__value = kwargs.get('value', None)
        self.__editable = kwargs.get('editable', True)
        self.__visible = kwargs.get('visible', True)
        self.events = set([])

    @property
    def view_id(self):
        return self.__view_id

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = self.on_value_set(v)

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, v):
        self.__visible = v

    @property
    def editable(self):
        return self.__editable

    @editable.setter
    def editable(self, v):
        self.__editable = v

    def add_event(self, name, callback):
        setattr(self, name, callback)
        self.events.add(name)

    def on_value_set(self, v):
        return v

    def serialize(self):
        self_type = type(self)
        result = {
            'className': f'{self_type.__module__}.{self_type.__name__}',
            'id': self.__view_id,
            'value': self.__value,
            'editable': self.__editable,
            'visible': self.__visible,
        }
        if len(self.events) > 0:
            result['events'] = list(self.events)
        return result


class SimpleLayout(BaseView):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._items: List[BaseView] = []

    @property
    def items(self):
        return self._items

    def add(self, view: BaseView):
        self.items.append(view)
        return self

    def serialize(self):
        result = super().serialize()
        result['childrenView'] = [i.serialize() for i in self._items]
        return result

    def get_child_by_id(self, view_id) -> BaseView:
        for i in self._items:
            if i.view_id == view_id:
                return i
        return None


class BaseTag(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        pass


class BaseSnippet(ABC, DjangoView):

    @property
    @abstractmethod
    def content_url(self) -> str:
        pass

    @property
    @abstractmethod
    def tags(self) -> List[BaseTag]:
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def layout(self) -> SimpleLayout:
        pass

    def get(self, request):
        return JsonResponse(data=self.layout.serialize())

    def post(self, request):
        json_request = json.loads(request.body)
        type = json_request.get('type')
        caller = json_request.get('caller')
        data = json_request.get('data')
        if not type or not caller:
            return JsonResponse(data={'error': 'can not parse request type or type'}, status=400)
        snippet_layout = self.layout
        for k, v in data.items():
            view = snippet_layout.get_child_by_id(k)
            if view:
                view.value = v
                setattr(self, k, view)
        caller = getattr(self, caller)
        if not caller:
            return JsonResponse(data={'error': 'can not found caller object'}, status=400)
        callback = getattr(caller, type)
        if not callback:
            return JsonResponse(data={'error': 'can not found callback for the given event type'}, status=400)
        callback()
        return JsonResponse(data=snippet_layout.serialize())
