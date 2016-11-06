from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
	personId = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=200, verbose_name='First Name', null=True, blank=True)
	middleName = models.CharField(max_length=200, verbose_name='Middle Name', null=True, blank=True)
	lastName = models.CharField(max_length=200, verbose_name='Last Name', null=True, blank=True)
class Contact(models.Model):
	contactId = models.AutoField(primary_key=True)
	email = models.EmailField(verbose_name='Email', null=True, blank=True)
	homePhone = models.IntegerField(verbose_name='Home Phone', null=True, blank=True)
	mobilePhone = models.IntegerField(verbose_name='Mobile Phone', null=True, blank=True)
class Location(models.Model):
	locationId = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200, verbose_name='Address', null=True, blank=True)
	city = models.CharField(max_length=200, verbose_name='City', null=True, blank=True)
	state = models.CharField(max_length=200, verbose_name='State', null=True, blank=True)
	zipCode = models.IntegerField(verbose_name='Zip Code', null=True, blank=True)
class Piece(models.Model):
	pieceId = models.AutoField(primary_key=True)
	isChinese = models.BooleanField(verbose_name='Chinese Piece')
	catalogue = models.CharField(max_length=200, verbose_name='Catalogue', null=True, blank=True)
	title = models.CharField(max_length=200, verbose_name='Title', null=True, blank=True)
	composer = models.CharField(max_length=200, verbose_name='Composer', null=True, blank=True)

class Parent(Person, Contact, Location):
	pass

class Teacher(Person, Contact, Location):
	pass

class Performer(Person):
	profileOwner = models.ForeignKey("Profile", related_name="profileOwner", verbose_name="Owner", null=True)
	teachers = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="teacher", verbose_name="Teacher's Information", null=True, blank=True)
	instrument = models.CharField(max_length=200, verbose_name="instrument", null=True, blank=True)
	accompanist = models.CharField(max_length=200, verbose_name="Accompanist", null=True, blank=True)
	group = models.CharField(max_length=200, verbose_name="Group", null=True, blank=True)
	piece1 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece1", verbose_name="First Piece", null=True, blank=True)
	piece2 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece2", verbose_name="Second Piece", null=True, blank=True)
	chinesePiece = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="chinesePiece", verbose_name="Chinese Piece", null=True, blank=True)

class Profile(models.Model):
	# Foreign Key Performer
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", verbose_name="User")
	performers = models.ForeignKey(Performer, related_name="performer", verbose_name="Performer", null=True, blank=True)
	parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name="parent", verbose_name="Parent", null=True, blank=True)