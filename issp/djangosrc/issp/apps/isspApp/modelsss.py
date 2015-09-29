from django.db import models

# Create your models here.

#### EXAMPLE MODEL#######
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=20, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self): #Python 2 is __unicode__
		return self.email


# class RackDetails(models.Model):
# 	name = models.CharField(max_lenght = 20)
# 	description = models.CharField(max_lenght = 20)

# 	def __str__(self):
# 		return self


# class Card(models.Model):
# 	rackdetail = models.ForeignKey(RackDetails):

# 	def __str__(self):
# 		return self


# class Version(models.Model):
# 	typeCard = models.CharField(max_length = 20)

# 	def __str__(self):
# 		return self


# class PositionInCard(models.Model):
	

# 	def __str__(self):
# 		return self
		

# class AssignedSensor(models.Model):
# 	positionwithinCard = models.ForeignKey(PositionInCard)
# 	cardId = models.ForeignKey(Card)

# 	def __str__(self):
# 		return self


# class Reading(models.Model):
# 	assignedSensor = models.ForeignKey(AssignedSensor)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	data = models.CharField(max_length= 20)

# 	def __str__(self):
# 		return self


# class Warnings(models.Model):
# 	reading = models.ForeignKey(Reading)
# 	warningTypes = models.ForeignKey(WarningTypes)

# 	def __str__(self):
# 		return self


# class WarningTypes(models.Model):
# 	descriptionWarning = models.CharField(max_length= 40)

# 	def __str__(self):
# 		return self
	