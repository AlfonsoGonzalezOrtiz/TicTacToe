# Generated by Django 3.2.20 on 2023-08-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20230825_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcador',
            name='playerO',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='marcador',
            name='playerX',
            field=models.IntegerField(default=0),
        ),
    ]