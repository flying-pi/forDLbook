# Generated by Django 2.0 on 2018-03-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor_neural_network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightmodel',
            name='accuracy',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='weightmodel',
            name='name',
            field=models.TextField(default='unknown'),
        ),
    ]
