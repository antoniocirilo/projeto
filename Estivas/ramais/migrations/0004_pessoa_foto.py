# Generated by Django 3.1.7 on 2021-03-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0003_pessoa_cc'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(null=True, upload_to='usuarios', verbose_name='Foto'),
        ),
    ]
