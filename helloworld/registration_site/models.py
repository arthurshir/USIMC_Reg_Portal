from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
	firstName = models.CharField(max_length=200, verbose_name='First Name', null=True, blank=True)
	middleName = models.CharField(max_length=200, verbose_name='Middle Name', null=True, blank=True)
	lastName = models.CharField(max_length=200, verbose_name='Last Name', null=True, blank=True)
	class Meta:
		abstract = True
	
class Contact(models.Model):
	email = models.EmailField(verbose_name='Email', null=True, blank=True)
	homePhone = models.IntegerField(verbose_name='Home Phone', null=True, blank=True)
	mobilePhone = models.IntegerField(verbose_name='Mobile Phone', null=True, blank=True)
	class Meta:
		abstract = True

class Location(models.Model):
	address = models.CharField(max_length=200, verbose_name='Address', null=True, blank=True)
	city = models.CharField(max_length=200, verbose_name='City', null=True, blank=True)
	state = models.CharField(max_length=200, verbose_name='State', null=True, blank=True)
	zipCode = models.IntegerField(verbose_name='Zip Code', null=True, blank=True)
	class Meta:
		abstract = True

class Piece(models.Model):
	catalogue = models.CharField(max_length=200, verbose_name='Catalogue', null=True, blank=True)
	title = models.CharField(max_length=200, verbose_name='Title', null=True, blank=True)
	composer = models.CharField(max_length=200, verbose_name='Composer', null=True, blank=True)

class ChinesePiece(models.Model):
	catalogue = models.CharField(max_length=200, verbose_name='Catalogue', null=True, blank=True)
	title = models.CharField(max_length=200, verbose_name='Title', null=True, blank=True)
	composer = models.CharField(max_length=200, verbose_name='Composer', null=True, blank=True)

class Parent(Person, Contact, Location):
	pass

class Teacher(Person, Contact, Location):
	pass

INSTRUMENT_CHOICES = (('0', 'Piano'), ('1', 'Violin'), ('2', 'Cello'), ('3', 'Viola'), ('4', 'Vocal'), ('5', 'Harp'), ('6', 'Guitar'), ('7', 'Gu-Zheng'), ('8', 'Pipa'), ('9', 'Er-Hu'), ('10', 'Chinese Ensemble'))
class Performer(Person):
	owningProfile = models.ForeignKey("Profile", related_name="profileOwner", verbose_name="Owner")
	_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="teacher", verbose_name="Teacher's Information")
	instrument = models.CharField(max_length=200, choices=INSTRUMENT_CHOICES, verbose_name="instrument", null=True, blank=True)
	accompanist = models.CharField(max_length=200, verbose_name="Accompanist", null=True, blank=True)
	group = models.CharField(max_length=200, verbose_name="Group", null=True, blank=True)
	piece1 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece1", verbose_name="First Piece")
	piece2 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece2", verbose_name="Second Piece")
	chinesePiece = models.OneToOneField(ChinesePiece, on_delete=models.CASCADE, related_name="chinesePiece", verbose_name="Chinese Piece")

class Profile(models.Model):
	# Foreign Key Performer
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", verbose_name="User")
	parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name="parent", verbose_name="Parent", null=True, blank=True)