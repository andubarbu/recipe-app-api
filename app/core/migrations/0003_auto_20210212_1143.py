# Generated by Django 2.1.15 on 2021-02-12 11:43

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
    ]