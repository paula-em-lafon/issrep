from django.db import models
from django.db.models.fields import AutoField

#cambios importantes: Agregado PK en cada tabla autosumante
#todos los modelos ahora regresan una variable especifica
#Cambié los campos para que se adecuen a standar de django.
#Card tiene ahora un pk separado del no. de serie.
#Warning type ahora tiene un campo llamado warning name

class RackDetails(models.Model):
    id_Rack = AutoField(primary_key = True)
    rack_name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 20)

    def __str__(self):
        return self.rack_name


class Card(models.Model):
    id_card = models.AutoField(primary_key = True)
    # The difference is one is a PK, the other an identificator for when the signal comes in
    card_serial = models.CharField(max_length = 6, unique = True)
    rack_detail = models.ForeignKey(RackDetails)

    def __str__(self):
        return self.rack_detail


class Version(models.Model):
    id_Version = models.AutoField(primary_key = True)
    type_card = models.CharField(max_length = 20)
    version_description = models.TextField()

    def __str__(self):
        return self.type_card


class PositionInCard(models.Model):
    id_position_in_card = models.IntegerField()

    def __str__(self):
        position_to_show = str(self.id_position_in_card)
        return position_to_show
        

class AssignedSensor(models.Model):
    id_assigned_sensor = models.AutoField(primary_key = True)
    position_within_card = models.ForeignKey(PositionInCard)
    cardId = models.ForeignKey(Card)

    def __str__(self):
        assigned_sensor = str(self.id_assigned_sensor)
        return self.assigned_sensor


class Reading(models.Model):
    id_reading = models.AutoField(primary_key = True)
    assigned_sensor = models.ForeignKey(AssignedSensor)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    data = models.CharField(max_length= 20)

    def __str__(self):
        reading = str(self.id_reading)
        return self.reading


class WarningTypes(models.Model):
    id_warning_type = AutoField(primary_key = True)
    warning_name = models.CharField(max_length = 30)
    description_warning = models.TextField()

    def __str__(self):
        return self.warning_name


class Warnings(models.Model):
    id_warning = models.AutoField(primary_key = True)
    reading = models.ForeignKey(Reading)
    warning_types = models.ForeignKey(WarningTypes)

    def __str__(self):
        warning = str(self.id_warning)
        return self.warning


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=20, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 2 is __unicode__
        return self.email