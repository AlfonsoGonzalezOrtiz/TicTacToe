# Generated by Django 4.2.4 on 2023-08-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("miapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tablero",
            name="a1",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="a2",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="a3",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="b2",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="b3",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="bl",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="c2",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="c3",
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name="tablero",
            name="cl",
            field=models.CharField(max_length=1),
        ),
    ]
