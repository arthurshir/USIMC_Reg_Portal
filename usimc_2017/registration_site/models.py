from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import datetime
import usimc_rules

#
# Choices
#


# Award Choices
CHINESE_AWARD = 'C'
JV_AWARD = 'J'
BACH_AWARD = 'B'
YOUNG_ARIST_AWARD = 'Y'

# Age Choices
CATEGORY_A = 'A'
CATEGORY_B = 'B'
CATEGORY_C = 'C'
CATEGORY_D = 'D'
CATEGORY_E = 'E'


# Award Categories
AWARD_CATEGORIES = (
    (YOUNG_ARIST_AWARD, 'Young Artist Award'),
    (CHINESE_AWARD, 'Chinese Award'),
    (BACH_AWARD, 'Bach Award'),
    (JV_AWARD, 'J.V. Award'),
)
AWARD_CATEGORIES_DICT = dict(AWARD_CATEGORIES)

# Age Categories
AGE_CATEGORIES = (
    (CATEGORY_A, 'A'),
    (CATEGORY_B, 'B'),
    (CATEGORY_C, 'C'),
    (CATEGORY_D, 'D'),
    (CATEGORY_E, 'E'),
)
AGE_CATEGORIES_DICT = dict(AGE_CATEGORIES)

#
# Custom Fields
#
class AutoDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()

#
# User Model
#

class USIMCUser(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name="usimc_user", verbose_name="User")
    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    is_admin = BooleanField(default=False)
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

    awards_applying_for = ArrayField(
        CharField( max_length=1, verbose_name='Awards Applying For', choices=AWARD_CATEGORIES)
    )
    instrument_category = CharField(choices=usimc_rules.INSTRUMENT_CATEGORY_CHOICES, max_length=100)
    age_category = CharField(choices=AGE_CATEGORIES, max_length=1)
    submitted = BooleanField(default=False)
    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    
    # Relations
    parent_contact = OneToOneField('ParentContact', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Parent Contact")
    teacher = OneToOneField('Teacher', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Teacher")
    lead_performer = OneToOneField('Person', null=True, on_delete=CASCADE, related_name="entry", verbose_name='Lead Performer')
    usimc_user = ForeignKey('USIMCUser', related_name='entry', verbose_name='USIMC User')
    # Pieces Performing -- Pieces Foreign Key
    # Applicants -- Ensember Members Foreign Key

    # Managers
    objects = EntryManager()

    class Meta:
        default_related_name =  'entries'

    def __unicode__(self):
        return self.usimc_user.user.username + "\'s Entry for " + self.instrument_category + " created at: " + self.created_at.strftime('%Y-%m-%d %H:%M')

class ParentContact(Model):
    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = CharField(null=True, blank=True, max_length=200, verbose_name='Email Address')
    phone_number = IntegerField(null=True, blank=True, verbose_name='Phone Number')

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        default_related_name = 'parent_contact'

class Piece(Model):

    # Attributes
    title = CharField(max_length=200, verbose_name='Title', blank=True, null=True)
    opus = CharField(max_length=200, verbose_name='Opus', blank=True, null=True)
    movement = CharField(max_length=200, verbose_name='Movement', blank=True, null=True)
    composer = CharField(max_length=200, verbose_name='Composer', blank=True, null=True)
    length = IntegerField(verbose_name='Length', null=True, blank=True)
    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    is_chinese = BooleanField(default=False, verbose_name='is Chinese Piece')


    # Relations
    entry = ForeignKey('Entry', verbose_name='Piece')

    class Meta:
        default_related_name = 'pieces'

    def __unicode__(self):
        return self.title + self.composer

class Teacher(Model):
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = EmailField(null=True, blank=True, verbose_name='Email')
    phone_number = IntegerField(null=True, blank=True, verbose_name='Phone Number')
    cmtanc_code = CharField(null=True, blank=True, max_length=200, verbose_name='Teacher\'s CMTANC Membership ID')

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

class Person(Model):

    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = EmailField(null=True, blank=True, verbose_name='Email')
    phone_number = IntegerField(null=True, blank=True, verbose_name='Phone Number')
    instrument = CharField(null=True, blank=True, max_length=200)
    address = CharField(null=True, blank=True, max_length=200)
    city = CharField(null=True, blank=True, max_length=200)
    state = CharField(null=True, blank=True, max_length=200)
    zip_code = CharField(null=True, blank=True, max_length=200)
    country = CharField(null=True, blank=True, max_length=200)
    birthday = DateField(null=True, blank=True)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        default_related_name = 'lead_performer'

class EnsembleMember(Model):

    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = EmailField(null=True, blank=True, verbose_name='Email')
    phone_number = IntegerField(null=True, blank=True, verbose_name='Phone Number')
    instrument = CharField(null=True, blank=True, max_length=200)
    birthday = DateField(null=True, blank=True)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    # Relations
    entry = ForeignKey('Entry', verbose_name='Ensemble Member')

    class Meta:
        default_related_name = 'ensemble_members'
