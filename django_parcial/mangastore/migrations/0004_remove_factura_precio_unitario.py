# Generated by Django 4.1.2 on 2023-06-19 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mangastore', '0003_alter_factura_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='precio_unitario',
        ),
    ]
