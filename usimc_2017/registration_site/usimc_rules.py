import json
import os
from pprint import pprint
import string
import datetime

# Define folder paths
folder_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(folder_path, 'static/registration_site/rules.json')

# Save data
with open(json_path) as json_data:
    data = json.load(json_data)

# Define Constants
RAW_JSON = data

INSTRUMENT_SOLO_CATEGORY_CHOICES = tuple(((str(k), str(v['name'])) for k,v in data['instrument_categories'].iteritems() if not v['ensemble']))
INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES = tuple(((str(k), str(v['name'])) for k,v in data['instrument_categories'].iteritems() if v['ensemble']))
INSTRUMENT_CATEGORY_CHOICES = INSTRUMENT_SOLO_CATEGORY_CHOICES + INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES

INSTRUMENT_SOLO_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_SOLO_CATEGORY_CHOICES)
INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES)
INSTRUMENT_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_CATEGORY_CHOICES)

# Basic retrieval functions
def print_data():
  pprint(data)

def get_instrument_category(instrument):
  print data['instrument_categories'][instrument]

def get_instrument_category_age_rules(instrument):
  # print data['instrument_categories'][instrument]['age_groups']
  # for index, age in enumerate(data['instrument_categories'][instrument]['age_groups']):
  #   print index, age

  return dict( (data['age_group_names'][index], age) for index, age in enumerate(data['instrument_categories'][instrument]['age_groups']))

def get_age_measurement_date_epoch():
  return data['age_measurement_cutoff_date']

def get_age_measurement_date():
  return datetime.datetime.fromtimestamp(data['age_measurement_date'])

def get_instrument_category_choices():
  return map(
    lambda x: str(x),
    data['instrument_categories'].keys()
    )

# print get_instrument_category_choices()