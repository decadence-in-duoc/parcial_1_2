# Generated by Django 4.1.2 on 2023-06-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangastore', '0002_alter_factura_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
