from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

#### Categories
#
#	Global declarations for all categories of pieces and performer/ ensemble types
#
CHINESE_SOLO = 'CS'
CHINESE_ENSEMBLE = 'CE'
VOCAL_SOLO = 'VS'
VOCAL_ENSEMBLE = 'VE'
NORMAL_SOLO = 'NS'
NORMAL_ENSEMBLE = 'NE'

PERFORMER_CATEGORIES = (
    (CHINESE_SOLO, 'Chinese Solo'),
    (CHINESE_ENSEMBLE, 'Chinese Ensemble'),
    (VOCAL_SOLO, 'Vocal Solo'),
    (VOCAL_ENSEMBLE, 'Vocal Ensemble'),
    (NORMAL_SOLO, 'Regular Instrument Solo'),
    (NORMAL_ENSEMBLE, 'Regular Instrument Ensemble'),
)


class USIMCUser(Model):
	# Foreign Key - entry
	pass

##	Single Entry
#	Represents a single entry
#		ex: a Chinese ensemble, a solo performer, a vocal solo performer, etc
#	Includes the Type of Award
class Entry(Model):
	usimc_user = ForeignKey('USIMCUser', related_name='entry', verbose_name='USIMC User')

	#### Additional Awards
	# Include Logic for Different Awards & Group Categories
    CHINESE_AWARD = 'C'
    JV_AWARD = 'J'
    BACH_AWARD = 'B'
    YOUNG_ARIST_AWARD = 'Y'
	CHOICES = (
		(CHINESE_AWARD, 'Chinese Award'),
		(JV_AWARD, 'J&V Foundation Award'),
		(BACH_AWARD, 'Bach Award'),
		(YOUNG_ARIST_AWARD, 'Young Artist Award'),
	)
	awards = ArrayField( CharField( max_length=2, verbose_name='Additional Awards' ) )

	# Pieces Foreign Key
	# Category Instrument Foreign Key

	#### Categories / Types
	# Only have 1 Type active at a time
	chinese_ensemble = OneToOneField(Teacher, on_delete=CASCADE, related_name="teacher", verbose_name="Teacher's Information")
	chinese_solo = 
	vocal_ensemble = 
	vocal_solo =
	normal_solo =
	normal_ensemble =



#### Piece Class
#
#	Piece includes catalogue, title, and composer, as well as typed
#
class Piece(Model):
    # Basic Information
    category = models.CharField(max_length=2, choices=PERFORMER_CATEGORIES)
	catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True)
	title = CharField(max_length=200, verbose_name='Title', blank=True)
	composer = CharField(max_length=200, verbose_name='Composer', blank=True)

	# Relation to Entry
	entry = models.ForeignKey(Entry)



#### Abstract Class
#
#	Used to include basic information for Performers and Ensembles
#
class Person(Model):
	firstName = CharField(max_length=200, verbose_name='First Name', blank=True)
	middleName = CharField(max_length=200, verbose_name='Middle Name', blank=True)
	lastName = CharField(max_length=200, verbose_name='Last Name', blank=True)
	class Meta:
		abstract = True

class PersonPerformer(Person):
    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


######## Solo Performer Classes
#
#
#

#### Normal Performer
#
# 	Elegible for All Awards
#
class NormalPerformer(Person):

#### Vocal Performer
#
# 	Elegible for All Awards
#
class VocalPerformer(Person):

#### Chinese Performer
#
# 	Only Elegible for Young Artist Award
#
class ChinesePerformer(Person):



######## Ensemble Classes

#### Normal Ensemble
#
# 	Elegible for All Awards
#
class NormalEnsemble(Model):
	members = GenericRelation(PersonPerformer)

#### Vocal Ensemble
#
# 	Elegible for All Awards
#
class VocalEnsemble(Model):
	members = GenericRelation(PersonPerformer)

#### Chinese Ensemble
#
# 	Only Elegible for Young Artist Award
#
class ChineseEnsemble(Model):
	members = GenericRelation(PersonPerformer)



class Piece(Model):
	catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True)
	title = CharField(max_length=200, verbose_name='Title', blank=True)
	composer = CharField(max_length=200, verbose_name='Composer', blank=True)

class Ensemble(Model):

	# Performer Foreign Key

## TODO: Try to figure out how to incorporate Generic Relation into your diff categories (Or if u even need it)
# Generic Relation: https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
class InstrumentCategory(Model):
    CHINESE_SOLO = 'CS'
    CHINESE_ENSEMBLE = 'CE'
    VOCAL_SOLO = 'VS'
    VOCAL_ENSEMBLE = 'VE'
    NORMAL_SOLO = 'NS'
    NORMAL_ENSEMBLE = 'NE'

    INSTRUMENT_TYPES = (
	    (CHINESE_SOLO, 'Chinese Solo'),
	    (CHINESE_ENSEMBLE, 'Chinese Ensemble'),
	    (VOCAL_SOLO, 'Vocal Solo'),
	    (VOCAL_ENSEMBLE, 'Vocal Ensemble'),
	    (NORMAL_SOLO, 'Regular Instrument Solo'),
	    (NORMAL_ENSEMBLE, 'Regular Instrument Ensemble'),
    )

    entry = models.ForeignKey(Entry)
    category_type = models.CharField(max_length=2, choices=INSTRUMENT_TYPES)

    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

class Contact(Model):
	email = EmailField(verbose_name='Email', blank=True)
	phone_number = IntegerField(verbose_name='Phone Number', blank=True)
	class Meta:
		abstract = True

class Performer(Contact):
	first_name = CharField(max_length=200, verbose_name='First Name', blank=False)
	middle_name = CharField(max_length=200, verbose_name='Middle Name', blank=True)
	last_name = CharField(max_length=200, verbose_name='Last Name', blank=False)
	# Depends on Category...
	instrument = models.CharField(max_length=200)
	teacher_first_name = CharField(max_length=200, verbose_name='Teacher\'s First Name', blank=False)
	teacher_middle_name = CharField(max_length=200, verbose_name='Teacher\'s Middle Name', blank=True)
	teacher_last_name = CharField(max_length=200, verbose_name='Teacher\'s Last Name', blank=False)
	teacher_code = CharField(max_length=200, verbose_name='Teacher\'s CMTANC Code', blank=True)






class ChineseSolo(Model):


class ChineseEnsemble(Model):

class ChineseSolo(Model):

class ChineseSolo(Model):


class Post(models.Model):


    likes = GenericRelation(InstrumentCategory)


class Award(Model):
	instrument = CharField(max_length=200, choices=INSTRUMENT_CHOICES, verbose_name="instrument", blank=True)


class Person(Model):
	firstName = CharField(max_length=200, verbose_name='First Name', blank=True)
	middleName = CharField(max_length=200, verbose_name='Middle Name', blank=True)
	lastName = CharField(max_length=200, verbose_name='Last Name', blank=True)
	class Meta:
		abstract = True
	
class Contact(Model):
	email = EmailField(verbose_name='Email', blank=True)
	homePhone = IntegerField(verbose_name='Home Phone', blank=True)
	mobilePhone = IntegerField(verbose_name='Mobile Phone', blank=True)
	class Meta:
		abstract = True

class Location(Model):
	address = CharField(max_length=200, verbose_name='Address', blank=True)
	city = CharField(max_length=200, verbose_name='City', blank=True)
	state = CharField(max_length=200, verbose_name='State', blank=True)
	zipCode = IntegerField(verbose_name='Zip Code', blank=True)
	class Meta:
		abstract = True

class Piece(Model):
	catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True)
	title = CharField(max_length=200, verbose_name='Title', blank=True)
	composer = CharField(max_length=200, verbose_name='Composer', blank=True)

class ChinesePiece(Model):
	catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True)
	title = CharField(max_length=200, verbose_name='Title', blank=True)
	composer = CharField(max_length=200, verbose_name='Composer', blank=True)

class Parent(Person, Contact, Location):
	pass

class Teacher(Person, Contact, Location):
	pass

INSTRUMENT_CHOICES = (('0', 'Piano'), ('1', 'Violin'), ('2', 'Cello'), ('3', 'Viola'), ('4', 'Vocal'), ('5', 'Harp'), ('6', 'Guitar'), ('7', 'Gu-Zheng'), ('8', 'Pipa'), ('9', 'Er-Hu'), ('10', 'Chinese Ensemble'))
class Performer(Person):
	owningProfile = ForeignKey("Profile", related_name="profileOwner", verbose_name="Owner")
	_teacher = OneToOneField(Teacher, on_delete=CASCADE, related_name="teacher", verbose_name="Teacher's Information")
	instrument = CharField(max_length=200, choices=INSTRUMENT_CHOICES, verbose_name="instrument", blank=True)
	accompanist = CharField(max_length=200, verbose_name="Accompanist", blank=True)
	group = CharField(max_length=200, verbose_name="Group", blank=True)
	piece1 = OneToOneField(Piece, on_delete=CASCADE, related_name="piece1", verbose_name="First Piece")
	piece2 = OneToOneField(Piece, on_delete=CASCADE, related_name="piece2", verbose_name="Second Piece")
	chinesePiece = OneToOneField(ChinesePiece, on_delete=CASCADE, related_name="chinesePiece", verbose_name="Chinese Piece")

class Profile(Model):
	# Foreign Key Performer
	user = OneToOneField(User, on_delete=CASCADE, related_name="user", verbose_name="User")
	parent = OneToOneField(Parent, on_delete=CASCADE, related_name="parent", verbose_name="Parent", blank=True)