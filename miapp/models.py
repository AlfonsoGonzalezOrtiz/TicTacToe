from django.db import models

# Create your models here.

class Tablero(models.Model):
    a1 = models.CharField(max_length=1)
    a2 = models.CharField(max_length=1)
    a3 = models.CharField(max_length=1)
    b1 = models.CharField(max_length=1)
    b2 = models.CharField(max_length=1)
    b3 = models.CharField(max_length=1)
    c1 = models.CharField(max_length=1)
    c2 = models.CharField(max_length=1)
    c3 = models.CharField(max_length=1)

    def __str__(self):
        return "%s%s%s%s%s%s%s%s%s" % (self.a1,self.a2,self.a3,self.b1,self.b2,self.b3,self.c1,self.c2,self.c3)

class Marcador(models.Model):
    jugadorX = models.IntegerField()
    jugadorO = models.IntegerField()

class Turno(models.Model):
    turno = models.BooleanField()

    def __str__(self):
        str = ''
        if self.turno:
            str = 'O'
        else:
            str = 'X'
        return str 