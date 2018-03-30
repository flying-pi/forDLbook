import hashlib
import os
import random
import string
from pathlib import Path
from urllib.request import Request

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse, Http404, HttpResponse
from django.views import View

from core.models import RawUserFile, ImageModel
from core.snippet_utils import get_installed_snippets, snippets_list_serialization
from fdlb_backend import settings

from PIL.Image import Image


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


class ImageView(View):
    def get(self, request, image_name):
        image_model = ImageModel.objects.filter(name=image_name)
        if len(image_model) == 0:
            raise Http404
        try:
            with open(image_model[0].image.path, "rb") as f:
                response =  HttpResponse(f.read(), content_type=image_model[0].mimetype)
                # response['Content-Disposition'] = f'inline;filename={image_model[0].name}'
                return response
        except IOError:
            raise Http404
        print('booo')
        # image = Image(image_model.first())
        # response = HttpResponse(content_type=image.mimetype)
        # image.image.save(response, image.mimetype)
        # return response
