# Generated by Django 3.1.7 on 2021-03-31 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0019_auto_20210331_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='ramal',
            field=models.CharField(default='', max_length=4, null=True, verbose_name='Ramal'),
        ),
    ]
