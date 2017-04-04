from __future__ import unicode_literals

from django.template.loader import render_to_string
from django.db.models import *
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
import datetime
import usimc_data
import usimc_rules
import phonenumbers

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

#
# Custom Fields
#
class AutoDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

#
# Helper Functions
#

def xstr(s):
    if s is None:
        return ''
    return str(s)

def string_to_date(s):
    try:
        return datetime.datetime.strptime(s, "%m-%d-%Y").date()
    except ValueError:
        return None

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
# Payment
#

class Charge(Model):
    usimc_user = ForeignKey('USIMCUser', on_delete=CASCADE, related_name="charges", verbose_name="USIMC User")
    entry = ForeignKey('Entry', on_delete=CASCADE, related_name="charge", verbose_name="Entry")
    charge_id = CharField(max_length=200)
    charge_amount = IntegerField()
    charge_customer = CharField(max_length=200)
    charge_description = CharField(max_length=500)
    charge_failure_message = CharField(max_length=500)
    charge_paid = BooleanField()
    charge_receipt_email = CharField(max_length=500)

    class Meta:
        default_related_name =  'charges'

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
    is_not_international = BooleanField(default=True)
    proof_of_age = FileField(null = True, blank = True)
    signature = CharField(max_length=500, blank=True, null=True)

    # Relations
    parent_contact = OneToOneField('ParentContact', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Parent Contact")
    teacher = OneToOneField('Teacher', null=True, on_delete=CASCADE, related_name="entry", verbose_name="Teacher")
    lead_performer = OneToOneField('Person', null=True, on_delete=CASCADE, related_name="entry", verbose_name='Lead Performer')
    usimc_user = ForeignKey('USIMCUser', related_name='entry', verbose_name='USIMC User')
    # pieces -- Pieces Foreign Key
    # ensemble_members -- Ensemble Members Foreign Key
    # charges -- Ensemble Members Foreign Key

    # Managers
    objects = EntryManager()

    # Functions

    def awards_include_youth(self):
        return usimc_rules.AWARD_CHOICE_YOUTH in self.awards_applying_for

    def validate(self):
        """Checks that all attributes are filled and birthdays and youtube_links are filled if Youth Award"""
        return not not (
            self.parent_contact.validate() and
            self.teacher.validate() and
            self.lead_performer.validate() and
            self.validate_youth_youtube_link_validation() and
            reduce((lambda x, y: x and y), map(lambda x: x.validate(), self.pieces.all())) and
            (reduce((lambda x, y: x and y), map(lambda x: x.validate(), self.ensemble_members.all())) if len(self.ensemble_members.all()) > 0 else True)
            )

    def validate_youth_youtube_link_validation(self):
        """Needs to have at least 2 entries with youtube links"""
        if usimc_rules.AWARD_CHOICE_YOUTH not in self.awards_applying_for:
            return True
        else:
            return len(
                filter(lambda x: x.youtube_link != None, self.pieces.all())
                ) >= 2

    def award_strings(self):
        return map(lambda x: usimc_rules.AWARD_CHOICES_DICT[x], self.awards_applying_for)

    def awards_string(self):
        return reduce((lambda x, y: x + ', ' + y), self.award_strings() )

    def instrument_category_string(self):
        return usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[self.instrument_category]

    def is_not_international_string(self):
        return 'No, U.S. Entry' if self.is_not_international else 'International Entry'

    def age_category_years(self):
        return usimc_rules.get_instrument_category_age_rules(self.instrument_category)[self.age_category]

    def age_category_string(self):
        return xstr(self.age_category) + ', below ' + xstr(self.age_category_years()) + ' years old'

    def price_per_competitor_per_award(self):
        price_per_competitor = 0
        pricing_dict = usimc_rules.get_instrument_category_prices(self.instrument_category)
        # If International
        if not self.is_not_international:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_INTERNATIONAL]
        # If CMTANC
        elif self.teacher.has_valid_cmtanc_code():
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_CMTANC]
        # If not CMTANC
        else:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_NO_CMTANC]
        return price_per_competitor

    def price_per_competitor_per_award_with_custom_values(self, is_not_international, cmtanc_code):
        price_per_competitor = 0
        pricing_dict = usimc_rules.get_instrument_category_prices(self.instrument_category)
        # If International
        if not is_not_international:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_INTERNATIONAL]
        # If CMTANC
        elif self.teacher.validate_cmtanc_code(cmtanc_code):
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_YES_CMTANC]
        # If not CMTANC
        else:
            price_per_competitor = pricing_dict[usimc_rules.KEY_PRICING_NO_CMTANC]
        return price_per_competitor

    def calculate_price_with_custom_values(self, num_ensemble_members, num_awards, is_not_international, cmtanc_code):
        # Price per competitor & award * (number of competitors) * (number of awards)
        return self.price_per_competitor_per_award_with_custom_values(is_not_international, cmtanc_code) * (num_ensemble_members + 1) * num_awards * 100        

    def calculate_price(self):
        # Price per competitor & award * (number of competitors) * (number of awards)
        return self.price_per_competitor_per_award() * (len(self.ensemble_members.all()) + 1) * len(self.awards_applying_for) * 100

    def is_ensemble(self):
        return usimc_rules.INSTRUMENT_CATEGORY_CHOICES_DICT[self.instrument_category] in usimc_rules.INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES_DICT.values()

    def create_pricing_string(self):
        return self.create_pricing_string_with_custom_values(len(self.ensemble_members.all()), len(self.awards_applying_for), self.is_not_international)

    def create_pricing_string(self):
        output = '$' + str(self.price_per_competitor_per_award()) + ' per contestant, per award category '
        if not self.is_not_international:
            output += ' for international entry\n'
        elif self.teacher.has_valid_cmtanc_code():
            output += ' (coached by Active CMTANC members)\n' if self.is_ensemble() else ' (students of Active CMTANC members)\n'
        else:
            output += ' (coached by Non-CMTANC members)\n' if self.is_ensemble() else ' (students of Non-CMTANC members)\n'
        output += 'x ' + str(len(self.ensemble_members.all()) + 1) + (' Contestants\n' if (len(self.ensemble_members.all()) + 1) > 1 else ' Contestant\n')
        output += 'x ' + str(len(self.awards_applying_for)) + (' Awards\n' if len(self.awards_applying_for) > 1 else ' Award\n')
        output += 'Total = $' + str(self.calculate_price()/100) + '\n'
        output += 'See http://usimc.org/rules-en.html for pricing details'
        return output

    def create_pricing_string_with_custom_values(self, num_ensemble_members, num_awards, is_not_international, cmtanc_code):
        output = '$' + str(self.price_per_competitor_per_award_with_custom_values(is_not_international, cmtanc_code)) + ' per contestant, per award category '
        if not is_not_international:
            output += ' for international entry\n'
        elif self.validate_cmtanc_code(cmtanc_code):
            output += ' (coached by Active CMTANC members)\n' if self.is_ensemble() else ' (students of Active CMTANC members)\n'
        else:
            output += ' (coached by Non-CMTANC members)\n' if self.is_ensemble() else ' (students of Non-CMTANC members)\n'
        output += 'x ' + str(num_ensemble_members + 1) + (' Contestants\n' if (num_ensemble_members + 1) > 1 else ' Contestant\n')
        output += 'x ' + str(num_awards) + (' Awards\n' if num_awards > 1 else ' Award\n')
        output += 'Total = $' + str(self.calculate_price_with_custom_values(num_ensemble_members, num_awards, is_not_international, cmtanc_code)/100) + '\n'
        output += 'See http://usimc.org/rules-en.html for pricing details'
        return output

    def basic_information_string(self):
        return 'USIMC entry ID:' + xstr(self.pk) + ',  Category: ' + self.instrument_category_string() + ", Age Category: " + self.age_category_string()

    def complete_description_string(self):
        context = {}  
        context['entry'] = self
        context['is_cmtanc_member_string'] = 'Yes' if self.teacher.has_valid_cmtanc_code() else 'No'
        context['awards_string'] = self.awards_string()
        context['age_category_string'] = self.age_category_string()
        context['instrument_category_string'] = self.instrument_category_string()
        context['is_not_international_string'] = self.is_not_international_string()
        context['lead_performer_birthday_string'] = self.lead_performer.birthday_string()
        context['lead_performer_home_address_string'] = self.lead_performer.home_address_string()
        context['ensemble_members'] = map(lambda x: {
                'first_name': x.first_name,
                'last_name': x.last_name,
                'instrument': x.instrument,
                'birthday_string': x.birthday_string()
                }, self.ensemble_members.all())
        context['pieces'] = map(lambda x: {
                'title': x.title,
                'opus': xstr(x.opus),
                'movement': xstr(x.movement),
                'composer': x.composer,
                'youtube_link': xstr(x.youtube_link),
                'length': xstr(x.minutes) + ' minutes ' + xstr(x.seconds) + ' seconds'
                }, self.pieces.all())
        return render_to_string('registration_site/application_submission/entry_complete_description.txt', context)

    def confirmation_email_string(self):
        context = {}  
        context['entry'] = self
        context['complete_description_string'] = self.complete_description_string()
        context['price'] = '$' + xstr(self.calculate_price()/100)
        context['pricing_string'] = self.create_pricing_string()
        context['charge_date'] = xstr(self.updated_at)
        return render_to_string('registration_site/application_submission/confirmation_email.txt', context)

    class Meta:
        default_related_name =  'entries'

    def __unicode__(self):
        return xstr(self.usimc_user.user.username) + "\'s Entry for " + xstr(self.instrument_category) + " created at: " + xstr(self.created_at.strftime('%Y-%m-%d %H:%M'))

class ParentContact(Model):
    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = CharField(null=True, blank=True, max_length=200, verbose_name='Email')
    phone_number = CharField(null=True, blank=True, max_length=200, verbose_name='Phone Number')

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    def validate(self):
        try:
            validate_email(self.email)
        except ValidationError:
            return False
        else:
            return not not (self.phone_number and self.first_name and self.last_name)


    def basic_information_string(self):
        return xstr(self.first_name) + ' ' + xstr(self.last_name) + ', ' + xstr(self.email) + ', ' + xstr(self.phone_number)

    class Meta:
        default_related_name = 'parent_contact'

class Piece(Model):

    # Attributes
    title = CharField(max_length=200, verbose_name='Title', blank=True, null=True)
    opus = CharField(max_length=200, verbose_name='Opus', blank=True, null=True)
    movement = CharField(max_length=200, verbose_name='Movement', blank=True, null=True)
    composer = CharField(max_length=200, verbose_name='Composer', blank=True, null=True)
    youtube_link = CharField(max_length=200, verbose_name='Youtube Link (Only needed for Young Artist Award Entry)', blank=True, null=True)
    minutes = CharField(max_length=6, verbose_name='min', null=True, blank=True)
    seconds = CharField(max_length=6, verbose_name='sec', null=True, blank=True)
    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    def validate(self):
        return not not(self.title and self.composer and self.minutes and self.seconds)

    # Relations
    entry = ForeignKey('Entry', verbose_name='Piece')

    def basic_information_string(self):
        return xstr(self.title) + ', opus: ' + xstr(self.opus) + ', movement: ' + xstr(self.movement) + ', composer: ' + xstr(self.composer)

    class Meta:
        default_related_name = 'pieces'

    def __unicode__(self):
        return xstr(self.title) + xstr(self.composer) + xstr(self.youtube_link)

class Teacher(Model):
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    email = CharField(null=True, blank=True, max_length=200, verbose_name='Email')
    cmtanc_code = CharField(null=True, blank=True, max_length=200, verbose_name='Teacher\'s CMTANC Membership ID')

    def has_valid_cmtanc_code(self):
        return self.cmtanc_code in usimc_data.get_cmtanc_codes()

    def validate_cmtanc_code(self, cmtanc_code):
        return cmtanc_code in usimc_data.get_cmtanc_codes()

    def validate(self):
        try:
            validate_email(self.email)
        except ValidationError:
            return False
        else:
            return not not (self.first_name and self.last_name and (self.has_valid_cmtanc_code() if self.cmtanc_code else True))

    def basic_information_string(self):
        return xstr(self.first_name) + ' ' + xstr(self.last_name) + ', ' + xstr(self.email) + ', ' + xstr(self.phone_number) + ', ' + xstr(self.cmtanc_code)

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
    month = CharField(null=True, blank=True, max_length=2)
    day = CharField(null=True, blank=True, max_length=2)
    year = CharField(null=True, blank=True, max_length=4)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    def birthday(self):
        if not (self.month and self.day and self.year):
            print "No month, day, year"
            return None
        else:
            return string_to_date(self.month + "-" + self.day + "-" + self.year)

    def validate_birthday(self, birthday):
        if not birthday:
            return False
        years = usimc_rules.get_instrument_category_age_rules(self.entry.instrument_category)[self.entry.age_category]
        cutoff = usimc_rules.get_age_measurement_date()
        cutoff = cutoff.replace(year=cutoff.year - years)
        return birthday >= cutoff

    def validate(self):
        return not not(self.first_name and self.last_name and self.instrument and self.address and self.city and self.state and self.zip_code and self.country and self.birthday() and self.validate_birthday(self.birthday()))

    def basic_information_string(self):
        output = xstr(self.first_name) + ' ' + xstr(self.last_name) + ', ' + xstr(self.instrument) + '\n'
        output += 'Address:\n' + xstr(self.address) + ', ' + xstr(self.city) + ' ' + xstr(self.state) + ', ' + xstr(self.zip_code) + ', ' + xstr(self.country) + '\n'
        output += 'Birthday:\n' + xstr(self.birthday())
        return output

    def birthday_string(self):
        return xstr(self.birthday())

    def home_address_string(self):
        return xstr(self.address) + ', ' + xstr(self.city) + ', ' + xstr(self.state) + ', ' + xstr(self.zip_code) + ', ' + xstr(self.country)

    class Meta:
        default_related_name = 'lead_performer'

class EnsembleMember(Model):

    # Attributes
    first_name = CharField(null=True, blank=True, max_length=200, verbose_name='First Name')
    last_name = CharField(null=True, blank=True, max_length=200, verbose_name='Last Name')
    instrument = CharField(null=True, blank=True, max_length=200)
    month = CharField(null=True, blank=True, max_length=2)
    day = CharField(null=True, blank=True, max_length=2)
    year = CharField(null=True, blank=True, max_length=4)

    created_at = DateTimeField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    # Relations
    entry = ForeignKey('Entry', verbose_name='Ensemble Member')

    def birthday(self):
        if not (self.month and self.day and self.year):
            return None
        else:
            return string_to_date(self.month + "-" + self.day + "-" + self.year)

    def validate_birthday(self, birthday):
        if not birthday:
            return False
        years = usimc_rules.get_instrument_category_age_rules(self.entry.instrument_category)[self.entry.age_category]
        cutoff = usimc_rules.get_age_measurement_date()
        cutoff = cutoff.replace(year=cutoff.year - years)
        return birthday >= cutoff

    def validate(self):
        return not not (self.first_name and self.last_name and self.instrument and self.birthday() and self.validate_birthday(self.birthday()))

    def birthday_string(self):
        return xstr(self.birthday())

    def basic_information_string(self):
        output = xstr(self.first_name) + ' ' + xstr(self.last_name) + ', ' + xstr(self.instrument) + '\n'
        output += 'Birthday:\n' + str(self.birthday())
        return output

    class Meta:
        default_related_name = 'ensemble_members'
