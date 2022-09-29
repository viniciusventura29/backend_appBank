# Generated by Django 4.1.1 on 2022-09-27 12:47

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, pixel_densities=[1, 2], upload_to='loja/imagens/'),
        ),
    ]