# Generated by Django 4.1.2 on 2023-06-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangastore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
