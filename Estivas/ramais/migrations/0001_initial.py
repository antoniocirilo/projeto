# Generated by Django 3.1.7 on 2021-03-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('setor', models.CharField(max_length=100, verbose_name='Setor')),
                ('cargo', models.CharField(max_length=50, verbose_name='Cargo')),
                ('matricula', models.CharField(max_length=10, verbose_name='Matricula')),
                ('ramal', models.CharField(max_length=5, verbose_name='Ramal')),
            ],
        ),
    ]
