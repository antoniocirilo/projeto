# Generated by Django 3.1.7 on 2021-04-20 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0030_informativo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aniversariante',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='aniversariante',
            name='nome',
        ),
    ]