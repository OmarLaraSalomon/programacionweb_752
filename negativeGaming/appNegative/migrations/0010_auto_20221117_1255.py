# Generated by Django 3.2.10 on 2022-11-17 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appNegative', '0009_auto_20221117_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={},
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='timestamp',
        ),
    ]
