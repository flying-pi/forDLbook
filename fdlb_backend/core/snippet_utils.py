import inspect
from importlib import import_module
from os import listdir
from os.path import isfile, join
from typing import List

from django.apps import apps

from core.base_components import BaseSnippet, BaseTag


def get_installed_snippets():
    snippets_items = []
    for name, _content in apps.app_configs.items():
        try:
            snippets_pkg_name = f'{name}.snippets'
            snippets_pkg = import_module(snippets_pkg_name)
            package_path = snippets_pkg.__path__[0]
            files = [f.replace('.py', '')
                     for f in listdir(package_path) if isfile(join(package_path, f)) and f.endswith('.py')]
            for file in files:
                module = import_module(f'{snippets_pkg_name}.{file}')
                members = inspect.getmembers(module)
                for name, body in members:
                    if not callable(body):
                        continue
                    if body.__name__ == BaseSnippet.__name__:
                        continue
                    if issubclass(body, BaseSnippet):
                        member_instance = body()
                        snippets_items.append(member_instance)
        except ModuleNotFoundError:
            continue
    return snippets_items


def tags_list_serialization(tags: List[BaseTag]) -> list:
    return [
        {
            'name': tag.name,
            'display_name': tag.display_name,
        }
        for tag in tags
    ]


def snippets_list_serialization(snippets: List[BaseSnippet]) -> list:
    return [
        {
            'name': snippet.display_name,
            'description': snippet.description,
            'url': snippet.content_url,
            'tags_list': tags_list_serialization(snippet.tags),
        }
        for snippet in snippets
    ]
