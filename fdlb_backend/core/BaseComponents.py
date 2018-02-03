from abc import ABC, abstractmethod
from typing import List, Any


class BaseTag(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def display_name(self) -> str:
        pass


class BaseSnippet(ABC):

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


