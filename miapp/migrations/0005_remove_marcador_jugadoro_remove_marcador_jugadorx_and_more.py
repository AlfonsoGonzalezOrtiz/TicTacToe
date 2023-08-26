# Generated by Django 4.2.4 on 2023-08-26 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0004_rename_bl_tablero_b1"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marcador",
            name="jugadorO",
        ),
        migrations.RemoveField(
            model_name="marcador",
            name="jugadorX",
        ),
        migrations.AddField(
            model_name="marcador",
            name="num_games",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="marcador",
            name="playerO",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="marcador",
            name="playerX",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="a1",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="a2",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="a3",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="b1",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="b2",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="b3",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="c1",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="c2",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="c3",
            field=models.CharField(default=" ", max_length=1),
        ),
        migrations.AlterField(
            model_name="turno",
            name="turno",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "marcador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="miapp.marcador"
                    ),
                ),
                (
                    "tablero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="miapp.tablero"
                    ),
                ),
                (
                    "turno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="miapp.turno"
                    ),
                ),
            ],
        ),
    ]