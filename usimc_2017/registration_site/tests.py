from django.test import TestCase
from .models import USIMCUser, Charge, Entry, ParentContact, Piece, Teacher, Person, EnsembleMember
from django.contrib.auth.models import User
import usimc_rules
from django.utils import timezone

class ModelValidationMethodTests(TestCase):
  user = None
  usimc_user = None
  entry = None
  def setUp(self):
    user = User.objects.create(username='test@gmail.com', email='test@gmail.com', password='password')
    usimc_user = USIMCUser.objects.create(user=user)

    entry = Entry.objects.create(
      awards_applying_for=[usimc_rules.AWARD_CHOICES[0][0], usimc_rules.AWARD_CHOICES[0][1]],
      instrument_category=usimc_rules.INSTRUMENT_CATEGORY_CHOICES[0][0],
      age_category=usimc_rules.AGE_CATEGORY_CHOICES[0][0],
      usimc_user=usimc_user,
      teacher = Teacher.objects.create(),
      lead_performer = Person.objects.create(),
      parent_contact = ParentContact.objects.create()
      )
    Piece.objects.create(entry = entry)
    Piece.objects.create(entry = entry)
    Piece.objects.create(entry = entry)
    EnsembleMember.objects.create(entry = entry)
    EnsembleMember.objects.create(entry = entry)
    EnsembleMember.objects.create(entry = entry)
    EnsembleMember.objects.create(entry = entry)
    entry.save()


  def test_ensemble_memmber(self):
    """EnsembleMember validation method works as expected"""
    entry = Entry.objects.all()[0]

    for ensemble_member in entry.ensemble_members.all():
      self.assertEqual(ensemble_member.validate(), False)

    for ensemble_member in entry.ensemble_members.all():
      ensemble_member.first_name = 'Test value'
      ensemble_member.last_name = 'Test value'
      ensemble_member.instrument = 'Test value'
      ensemble_member.birthday = timezone.now().date()
      ensemble_member.save()

    for ensemble_member in entry.ensemble_members.all():
      self.assertEqual(ensemble_member.validate(), True)

  def test_pieces(self):
    """Piece validation method works as expected"""
    entry = Entry.objects.all()[0]

    for piece in entry.pieces.all():
      self.assertEqual(piece.validate(), False)

    for piece in entry.pieces.all():
      piece.title = 'Test value'
      piece.composer = 'Test value'
      piece.minutes = 1
      piece.seconds = 1
      piece.save()

    for piece in entry.pieces.all():
      self.assertEqual(piece.validate(), True)

  def test_lead_competitor(self):
    """LeadCompetitor validation method works as expected"""
    entry = Entry.objects.all()[0]

    self.assertEqual(entry.lead_performer.validate(), False)

    entry.lead_performer.first_name = 'Test value'
    entry.lead_performer.last_name = 'Test value'
    entry.lead_performer.instrument = 'Test value'
    entry.lead_performer.address = 'Test value'
    entry.lead_performer.city = 'Test value'
    entry.lead_performer.state = 'Test value'
    entry.lead_performer.zip_code = 'Test value'
    entry.lead_performer.country = 'Test value'
    entry.lead_performer.birthday = timezone.now().date()
    self.assertEqual(entry.lead_performer.validate(), True)

    print 'birthday', entry.lead_performer.birthday
    entry.lead_performer.save()

  def test_teacher(self):
    """Teacher validation method works as expected"""
    entry = Entry.objects.all()[0]

    self.assertEqual(entry.teacher.validate(), False)

    entry.teacher.first_name = 'Test value'
    entry.teacher.last_name = 'Test value'
    entry.teacher.email = 'Test value'
    self.assertEqual(entry.teacher.validate(), False)

    entry.teacher.email = 'test@gmail.com'
    self.assertEqual(entry.teacher.validate(), True)

    entry.teacher.save()

  def test_parent_contact(self):
    """ParentContact validation method works as expected"""
    entry = Entry.objects.all()[0]

    self.assertEqual(entry.parent_contact.validate(), False)

    entry.parent_contact.first_name = 'Test value'
    entry.parent_contact.last_name = 'Test value'
    entry.parent_contact.email = 'Test value'
    entry.parent_contact.phone_number = '5106768998'
    self.assertEqual(entry.parent_contact.validate(), False)

    #TODO: get phone number validation to work
    entry.parent_contact.email = 'test@gmail.com'
    self.assertEqual(entry.parent_contact.validate(), True)

    entry.parent_contact.save()

  def test_entry(self):
    """Entry validation method works as expected"""
    entry = Entry.objects.all()[0]

    self.test_ensemble_memmber()
    self.test_pieces()
    self.test_lead_competitor()
    self.test_teacher()
    self.test_parent_contact()
    
    self.assertEqual(entry.validate(), True)
