from abc import ABC, abstractmethod
from typing import List
import json

from django.http import JsonResponse
from django.views import View as DjangoView


class BaseView(object):

    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__view_id = kwargs.get('view_id', None)
        self.__value = kwargs.get('value', None)
        self.__editable = kwargs.get('editable', True)
        self.label = kwargs.get('label', '')

    @property
    def view_id(self):
        return self.__view_id

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @property
    def editable(self):
        return self.__editable

    def serialize(self):
        self_type = type(self)
        return {
            'className': f'{self_type.__module__}.{self_type.__name__}',
            'id': self.__view_id,
            'value': self.__value,
            'label': self.label,
            'editable': self.__editable,
        }


class SimpleLayout(object):
    def __init__(self):
        self._items: List[BaseView] = []

    @property
    def items(self):
        return self._items

    def add(self, view: BaseView):
        self.items.append(view)
        return self

    def serialize(self):
        self_type = type(self)
        return {
            'id': None,
            'className': f'{self_type.__module__}.{self_type.__name__}',
            'childrenView': [i.serialize() for i in self._items]
        }


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
        return JsonResponse(data={'layout': self.layout.serialize()})

    def process_request(self, data) -> SimpleLayout:
        return SimpleLayout()

    def post(self, request):
        state = json.loads(request.body)['state']
        return JsonResponse(data={'responseLayout': self.process_request(state).serialize()})