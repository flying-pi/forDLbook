from django.db import models

# Create your models here.
from django.db.models import Model, TextField, CharField


class RawUserFile(Model):
    hash = CharField(db_index=True, max_length=32)
    filename = TextField()
