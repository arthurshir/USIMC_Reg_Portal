from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import datetime
import usimc_rules
from phonenumber_field.modelfields import PhoneNumberField

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
        CharField( max_length=20, verbose_name='Awards Applying For', choices=usimc_rules.AWARD_CHOICES)
    )
    instrument_category = CharField(choices=usimc_rules.INSTRUMENT_CATEGORY_CHOICES, max_length=100)
    age_category = CharField(choices=usimc_rules.AGE_CATEGORY_CHOICES, max_length=1)
    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    submitted = BooleanField(default=False)
    is_not_international = BooleanField(default=False)
    
    # Relations
    parent_contact = OneToOneField('ParentContact', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Parent Contact")
    teacher = OneToOneField('Teacher', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Teacher")
    lead_performer = OneToOneField('Person', null=True, on_delete=CASCADE, related_name="entry", verbose_name='Lead Performer')
    usimc_user = ForeignKey('USIMCUser', related_name='entry', verbose_name='USIMC User')
    # Pieces Performing -- Pieces Foreign Key
    # Applicants -- Ensemble Members Foreign Key

    # Managers
    objects = EntryManager()

    # Functions
    def awards_string(self):
        award_strings = map(lambda x: usimc_rules.AWARD_CHOICES_DICT[x], self.awards_applying_for)
        return reduce((lambda x, y: x + ', ' + y), award_strings )

    def price_per_competitor_per_award(self):
        price_per_competitor = 0
        pricing_dict = usimc_rules.get_instrument_category_prices(self.instrument_category)
        # If International
        if not self.is_not_international:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_INTERNATIONAL]
        # If CMTANC
        elif self.teacher.cmtanc_code:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_CMTANC]
        # If not CMTANC
        else:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_NO_CMTANC]
        return price_per_competitor

    def calculate_price(self):
        # Price per competitor & award * (number of competitors) * (number of awards)
        return self.price_per_competitor_per_award() * (len(self.ensemble_members.all()) + 1) * len(self.awards_applying_for)

    def is_ensemble(self):
        return usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[self.instrument_category] in usimc_rules.INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES_DICT.values()

    def calculate_price_string(self):
        output = '$' + str(self.price_per_competitor_per_award()) + ' per contestant per award '
        if not self.is_not_international:
            output += ' for international entry\n'
        elif self.teacher.cmtanc_code:
            output += ' for CMTANC member\n'
        else:
            output += '\n'
        output += 'x ' + str(len(self.ensemble_members.all()) + 1) + (' Contestants\n' if (len(self.ensemble_members.all()) + 1) > 1 else ' Contestant\n')
        output += 'x ' + str(len(self.awards_applying_for)) + (' Awards\n' if len(self.awards_applying_for) > 1 else ' Award\n')
        output += 'Total = $' + str(self.calculate_price())
        return output

    class Meta:
        default_related_name =  'entries'

    def __unicode__(self):
        return self.usimc_user.user.username + "\'s Entry for " + self.instrument_category + " created at: " + self.created_at.strftime('%Y-%m-%d %H:%M')

class ParentContact(Model):
    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = EmailField(null=True, blank=True, verbose_name='Email')
    phone_number = CharField(null=True, blank=True, max_length=200, verbose_name='Phone Number')

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
    is_chinese = BooleanField(default=False, verbose_name='This is a Chinese Piece')


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
    phone_number = CharField(null=True, blank=True, max_length=200, verbose_name='Phone Number')
    cmtanc_code = CharField(null=True, blank=True, max_length=200, verbose_name='Teacher\'s CMTANC Membership ID')

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

class Person(Model):

    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    instrument = CharField(null=True, blank=True, max_length=200)
    address = CharField(null=True, blank=True, max_length=200)
    city = CharField(null=True, blank=True, max_length=200)
    state = CharField(null=True, blank=True, max_length=200)
    zip_code = CharField(null=True, blank=True, max_length=200)
    country = CharField(null=True, blank=True, max_length=200)
    birthday = DateTimeField(null=True, blank=True)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        default_related_name = 'lead_performer'

class EnsembleMember(Model):

    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    instrument = CharField(null=True, blank=True, max_length=200)
    birthday = DateTimeField(null=True, blank=True)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    # Relations
    entry = ForeignKey('Entry', verbose_name='Ensemble Member')

    class Meta:
        default_related_name = 'ensemble_members'
