# Generated by Django 3.1.7 on 2021-03-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0010_auto_20210331_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='Email'),
        ),
    ]
