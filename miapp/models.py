from django.db import models
from miapp.constants import EMPTY_CELL
# Create your models here.

class Tablero(models.Model):
    a1 = models.CharField(max_length=1, default=EMPTY_CELL)
    a2 = models.CharField(max_length=1, default=EMPTY_CELL)
    a3 = models.CharField(max_length=1, default=EMPTY_CELL)
    b1 = models.CharField(max_length=1, default=EMPTY_CELL)
    b2 = models.CharField(max_length=1, default=EMPTY_CELL)
    b3 = models.CharField(max_length=1, default=EMPTY_CELL)
    c1 = models.CharField(max_length=1, default=EMPTY_CELL)
    c2 = models.CharField(max_length=1, default=EMPTY_CELL)
    c3 = models.CharField(max_length=1, default=EMPTY_CELL)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_fields_length()

    def validate_fields_length(self):
        max_length = 1
        for field_name in self._meta.get_fields():
            if isinstance(field_name, models.CharField):
                field_value = getattr(self, field_name.attname)
                if len(field_value) > max_length:
                    raise ValueError(f"El campo {field_name.attname} excede la longitud máxima permitida.")

    def __str__(self):
        return "%s%s%s%s%s%s%s%s%s" % (self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3)

class Marcador(models.Model):
    playerX = models.IntegerField(default=0)
    playerO = models.IntegerField(default=0)
    num_games = models.IntegerField(default=0)

class Turno(models.Model):
    turno = models.BooleanField(blank=True, null=True)

    def __str__(self):
        if self.turno is None:
            return ' '
        elif self.turno:
            return 'O'
        else:
            return 'X'