# Generated by Django 4.2.2 on 2023-07-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangastore', '0008_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=1000),
        ),
    ]
