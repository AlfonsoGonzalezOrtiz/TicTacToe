# Generated by Django 4.2.4 on 2023-08-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0005_remove_marcador_jugadoro_remove_marcador_jugadorx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="turno",
            name="turno",
            field=models.BooleanField(blank=True, default=1),
        ),
    ]