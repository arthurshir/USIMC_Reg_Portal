from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
	personId = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=200, verbose_name='First Name')
	middleName = models.CharField(max_length=200, verbose_name='Middle Name')
	lastName = models.CharField(max_length=200, verbose_name='Last Name')
class Contact(models.Model):
	contactId = models.AutoField(primary_key=True)
	email = models.EmailField(verbose_name='Email')
	homePhone = models.IntegerField(verbose_name='Home Phone')
	mobilePhone = models.IntegerField(verbose_name='Mobile Phone')
class Location(models.Model):
	locationId = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200, verbose_name='Address')
	city = models.CharField(max_length=200, verbose_name='City')
	state = models.CharField(max_length=200, verbose_name='State')
	zipCode = models.IntegerField(verbose_name='Zip Code')
class Piece(models.Model):
	pieceId = models.AutoField(primary_key=True)
	isChinese = models.BooleanField(verbose_name='Chinese Piece')
	catalogue = models.CharField(max_length=200, verbose_name='Catalogue')
	title = models.CharField(max_length=200, verbose_name='Title')
	composer = models.CharField(max_length=200, verbose_name='Composer')


class Parent(Person, Contact, Location):
	pass

class Teacher(Person, Contact, Location):
	pass

class Performer(Person):
	teachers = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="teacher", verbose_name="Teacher's Information")
	instrument = models.CharField(max_length=200, verbose_name="instrument")
	accompanist = models.CharField(max_length=200, verbose_name="Accompanist")
	group = models.CharField(max_length=200, verbose_name="Group")
	piece1 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece1", verbose_name="First Piece")
	piece2 = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="piece2", verbose_name="Second Piece", null=True)
	chinesePiece = models.OneToOneField(Piece, on_delete=models.CASCADE, related_name="chinesePiece", verbose_name="Chinese Piece", null=True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", verbose_name="User")
	performers = models.ForeignKey(Performer, related_name="performer", verbose_name="Performer", null=True)
	parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name="parent", verbose_name="Parent")