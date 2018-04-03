from django.db import models

# Create your models here.
from django.db.models import Model, TextField, BinaryField, FloatField


class WeightModel(Model):
    name = TextField(default='unknown')
    classificator_provider = TextField(blank=False)
    shape = BinaryField(blank=True)
    body = BinaryField()
    accuracy = FloatField(default=-1)
    lambda_value = FloatField(default=-1)
    learn_rate = FloatField(default=-1)
