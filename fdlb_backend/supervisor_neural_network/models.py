from django.db import models

# Create your models here.
from django.db.models import Model, TextField, BinaryField, FloatField


class WeightModel(Model):
    name = TextField(default='unknown')
    shape = BinaryField()
    body = BinaryField()
    accuracy = FloatField(default=-1)
