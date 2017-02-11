from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

#
# Choices
#

# Performer Choices
PIANO = 'PI'
VIOLIN = 'VN'
VIOLA = 'VA'
CELLO = 'CE'
CHINESE_TRADITIONAL_INSTRUMENT = 'CN'
MARIMBA = 'MA'
FLUTE = 'FL'
CLARINET = 'CL'
VOCAL = 'VO'
CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE = 'CNE'
CHAMBER_ENSEMBLE = 'CHE'
VOCAL_ENSEMBLE = 'VOE'

# Award Choices
CHINESE_AWARD = 'C'
JV_AWARD = 'J'
BACH_AWARD = 'B'
YOUNG_ARIST_AWARD = 'Y'

# Age Choices
_8_OR_UNDER = 8
_9_OR_UNDER = 9
_10_OR_UNDER = 10
_11_OR_UNDER = 11
_12_OR_UNDER = 12
_13_OR_UNDER = 13
_14_OR_UNDER = 14
_15_OR_UNDER = 15
_17_OR_UNDER = 17
_22_OR_UNDER = 22
_30_OR_UNDER = 30

# Performer Categories
PERFORMER_CATEGORIES = (
    (PIANO, 'Piano'),
    (VIOLIN, 'Violin'),
    (VIOLA, 'Viola'),
    (CELLO, 'Cello'),
    (CHINESE_TRADITIONAL_INSTRUMENT, 'Chinese Traditional Instrument'),
    (MARIMBA, 'Marimba'),
    (FLUTE, 'Flute'),
    (CLARINET, 'Clarinet'),
    (VOCAL, 'Vocal'),
    (CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE, 'Chinese Traditional Instruments Ensemble'),
    (CHAMBER_ENSEMBLE, 'Chamber Ensemble'),
    (VOCAL_ENSEMBLE, 'Vocal Ensemble'),
)

# Instrument Categories
values_to_remove = [ CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE, CHAMBER_ENSEMBLE, VOCAL_ENSEMBLE ]
INSTRUMENT_CHOICES = tuple(x for x in PERFORMER_CATEGORIES if x[0] not in values_to_remove)

# Award Categories
AWARD_CATEGORIES = (
    (CHINESE_AWARD, 'Chinese Award'),
    (JV_AWARD, 'J&V Foundation Award'),
    (BACH_AWARD, 'Bach Award'),
    (YOUNG_ARIST_AWARD, 'Young Artist Award'),
)

# Age Categories
AGE_CATEGORIES = (
    (_8_OR_UNDER, 'Age 8 or under'),
    (_9_OR_UNDER, 'Age 9 or under'),
    (_10_OR_UNDER, 'Age 10 or under'),
    (_11_OR_UNDER, 'Age 11 or under'),
    (_12_OR_UNDER, 'Age 12 or under'),
    (_13_OR_UNDER, 'Age 13 or under'),
    (_14_OR_UNDER, 'Age 14 or under'),
    (_15_OR_UNDER, 'Age 15 or under'),
    (_17_OR_UNDER, 'Age 17 or under'),
    (_22_OR_UNDER, 'Age 22 or under'),
    (_30_OR_UNDER, 'Age 30 or under'),
)

#
# User Model
#

class USIMCUserManager(Manager):
    def create_user(self, user):
        return USIMCUser.objects.get_or_create(user=user)

class USIMCUser(Model):
    user = OneToOneField(User, on_delete=CASCADE, verbose_name="User")
    # Foreign Key Entry

    # Managers
    objects = USIMCUserManager()

    class Meta:
        default_related_name =  'usimc_user'

#
# Entry Model & Related Models
#

class EntryManager(Manager):
    def get_unsubmitted(self):
        try:
            return self.get_queryset().filter(submitted=False).order_by('category')[0]
        except:
            return None

    def get_submitted(self):
        try:
            return self.get_queryset().filter(submitted=True).order_by('category')[0]
        except:
            return None

class Entry(Model):
    # Attribs
    awards_applying_for = ArrayField( CharField(max_length=1, verbose_name='Awards Applying For', choices=AWARD_CATEGORIES) , null=True)
    instrument_category = CharField(max_length=3, choices=PERFORMER_CATEGORIES, null=True)
    age_category = IntegerField(choices=AGE_CATEGORIES, null=True)
    submitted = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    # Relations
    usimc_user = ForeignKey('USIMCUser', related_name='entry', verbose_name='USIMC User')
    # Pieces Performing -- Pieces Foreign Key
    # Applicants -- Person Foreign Key

    # Managers
    objects = EntryManager()

    class Meta:
        default_related_name =  'entries'
    def __unicode__(self):
        return self.usimc_user.user.username + "\'s Entry for " + self.instrument_category + " created at: " + self.created_at.strftime('%Y-%m-%d %H:%M')

class Piece(Model):

    # Attributes
    catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True, null=True)
    title = CharField(max_length=200, verbose_name='Title', null=True)
    composer = CharField(max_length=200, verbose_name='Composer', null=True)

    # Relations
    entry = ForeignKey('Entry', verbose_name='Piece', null=True)

    class Meta:
        default_related_name = 'pieces'

class Person(Model):

    # Attributes
    first_name = CharField(max_length=200, verbose_name='First Name', null=True)
    middle_name = CharField(max_length=200, verbose_name='Middle Name', null=True)
    last_name = CharField(max_length=200, verbose_name='Last Name', null=True)
    email = EmailField(verbose_name='Email', null=True)
    phone_number = IntegerField(verbose_name='Phone Number', null=True)
    instrument = CharField(max_length=2, choices=INSTRUMENT_CHOICES, null=True)
    teacher_first_name = CharField(max_length=200, verbose_name='Teacher\'s First Name', null=True)
    teacher_middle_name = CharField(max_length=200, verbose_name='Teacher\'s Middle Name', blank=True, null=True)
    teacher_last_name = CharField(max_length=200, verbose_name='Teacher\'s Last Name', null=True)
    teacher_code = CharField(max_length=200, verbose_name='Teacher\'s CMTANC Code', blank=True, null=True)

    # Relations
    entry = ForeignKey('Entry', verbose_name='USIMC User', null=True)

    class Meta:
        default_related_name = 'people'