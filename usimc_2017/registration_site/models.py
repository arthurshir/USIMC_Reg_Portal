from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


#
# Choices
#

# Performer Choices
PIANO = 'PI'
VIOLIN = 'VN'
VIOLA = 'VA'
CELLO = 'CE'
CHINESE_TRADITIONAL_INSTRUMENTS = 'CN'
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
    (CHINESE_TRADITIONAL_INSTRUMENTS, 'Chinese Traditional Instruments'),
    (MARIMBA, 'Marimba'),
    (FLUTE, 'Flute'),
    (CLARINET, 'Clarinet'),
    (VOCAL, 'Vocal'),
    (CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE, 'Chinese Traditional Instruments Ensemble'),
    (CHAMBER_ENSEMBLE, 'Chamber Ensemble'),
    (VOCAL_ENSEMBLE, 'Vocal Ensemble'),
)

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

class USIMCUser(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="user", verbose_name="User")
    # Foreign Key Entry

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
    awards_applying_for = ArrayField( CharField( max_length=1, verbose_name='Awards Applying For', choices=AWARD_CATEGORIES) )
    instrument_category = CharField(choices=PERFORMER_CATEGORIES, max_length=4)
    age_category = IntegerField(choices=AGE_CATEGORIES)
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
        default_related_name =  'entry'

    def __unicode__(self):
        return self.usimc_user.user.username + "\'s Entry for " + self.category + " creatd at: " + created_at.strftime('%Y-%m-%d %H:%M')

class Piece(Model):

    # Attributes
    catalogue = CharField(max_length=200, verbose_name='Catalogue', blank=True)
    title = CharField(max_length=200, verbose_name='Title')
    composer = CharField(max_length=200, verbose_name='Composer')

    # Relations
    entry = ForeignKey('Entry', verbose_name='Piece')

    class Meta:
        default_related_name = 'piece'

class Person(Model):

    # Attributes
    firstName = CharField(max_length=200, verbose_name='First Name')
    middleName = CharField(max_length=200, verbose_name='Middle Name')
    lastName = CharField(max_length=200, verbose_name='Last Name')
    email = EmailField(verbose_name='Email')
    phone_number = IntegerField(verbose_name='Phone Number')
    instrument = CharField(max_length=200)
    teacher_first_name = CharField(max_length=200, verbose_name='Teacher\'s First Name')
    teacher_middle_name = CharField(max_length=200, verbose_name='Teacher\'s Middle Name', blank=True)
    teacher_last_name = CharField(max_length=200, verbose_name='Teacher\'s Last Name')
    teacher_code = CharField(max_length=200, verbose_name='Teacher\'s CMTANC Code', blank=True)

    # Relations
    entry = ForeignKey('Entry', verbose_name='USIMC User')

    class Meta:
        default_related_name = 'person'