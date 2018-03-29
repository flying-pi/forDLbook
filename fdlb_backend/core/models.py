from django.core.files.storage import FileSystemStorage
# Create your models here.
from django.db.models import Model, TextField, CharField, ImageField

from fdlb_backend import settings


class RawUserFile(Model):
    hash = CharField(db_index=True, max_length=32)
    filename = TextField()


fs = FileSystemStorage(location=settings.IMG_FILE_DIR)


class ImageModel(Model):
    name = TextField(default='')
    image = ImageField(blank=False, storage=fs)
    mimetype = TextField(blank=False)
