# Generated by Django 3.1.7 on 2021-04-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ramais', '0029_aniversariante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=15, verbose_name='Mes')),
                ('fotoinformativo', models.ImageField(upload_to='informativo', verbose_name='fotoinformativo')),
                ('anexo', models.FileField(upload_to='informativo', verbose_name='Anexoinformativo')),
            ],
        ),
    ]
