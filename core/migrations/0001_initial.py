# Generated by Django 3.0.8 on 2020-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColumaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecoluna', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Coluna',
                'verbose_name_plural': 'Colunas',
                'ordering': ['nomecoluna'],
            },
        ),
    ]
