# Generated by Django 3.1.7 on 2021-03-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0018_auto_20210331_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='ramal',
            field=models.CharField(max_length=4, null=True, verbose_name='Ramal'),
        ),
    ]