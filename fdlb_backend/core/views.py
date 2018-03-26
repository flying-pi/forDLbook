import hashlib
import os
import random
import string
from pathlib import Path
from urllib.request import Request

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.views import View

from core.models import RawUserFile
from core.snippet_utils import get_installed_snippets, snippets_list_serialization
from fdlb_backend import settings


class RootView(View):

    def get(self, request: Request) -> JsonResponse:
        snippets = snippets_list_serialization(get_installed_snippets())
        return JsonResponse(data={'snippets': snippets})


class FileView(View):

    def save_file(self, file: InMemoryUploadedFile, filename = None) -> str:
        """
        Save fule.
        :param file: file from the request.
        :return: path to saved file.
        """
        os.makedirs(os.path.dirname(settings.UPLOADED_FILE_DIR), exist_ok=True)

        if not filename:
            while True:
                filename = settings.UPLOADED_FILE_DIR + ''.join(random.choices(string.ascii_lowercase, k=42))
                if not os.path.isfile(filename):
                    break
            name_puts = file.name.split('.')
            if len(name_puts) > 1:
                filename = f'{filename}.{name_puts[-1]}'
        with open(filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return filename

    def post(self, request: Request):
        file = request.FILES['file']
        hash = hashlib.md5(file.read()).hexdigest()
        exist_files = RawUserFile.objects.filter(hash = hash)
        file.seek(0)
        if exist_files.exists():
            filename = exist_files.first().filename
            if not Path(filename).is_file():
                self.save_file(file, filename)
            file_id = exist_files.first().id
        else:
            filename = self.save_file(file)
            new_file_record = RawUserFile.objects.create(hash = hash,filename= filename)
            file_id = new_file_record.id

        return JsonResponse(data={'fileID': file_id})

    pass
