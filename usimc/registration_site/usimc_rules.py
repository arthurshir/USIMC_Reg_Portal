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

INSTRUMENT_SOLO_CATEGORY_CHOICES = sorted(tuple(((str(k), str(v['name'])) for k,v in data['instrument_categories'].items() if not v['ensemble'])))
INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES = sorted(tuple(((str(k), str(v['name'])) for k,v in data['instrument_categories'].items() if v['ensemble'])))
INSTRUMENT_CATEGORY_CHOICES = sorted(tuple(((str(k), str(v['name'])) for k,v in data['instrument_categories'].items())))
INSTRUMENT_SOLO_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_SOLO_CATEGORY_CHOICES)
INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_ENSEMBLE_CATEGORY_CHOICES)
INSTRUMENT_CATEGORY_CHOICES_DICT = dict(INSTRUMENT_CATEGORY_CHOICES)

INSTRUMENT_CHOICE_CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE = 'chinese_traditional_instruments_ensemble'
INSTRUMENT_CHOICE_CHAMBER_ENSEMBLE = 'chamber_ensemble'

AGE_CATEGORY_CHOICES = sorted(tuple(((str(x), str(x)) for x in data['age_group_names'])))
AGE_CATEGORY_CHOICES_DICT = dict(AGE_CATEGORY_CHOICES)

AWARD_CHOICES = sorted(tuple(((str(x), data['awards'][x]['name']) for x in data['awards'])), reverse=True)
AWARD_CHOICES_DICT = dict(AWARD_CHOICES)
AWARD_CHOICE_YOUTH = 'young_artist_award'
AWARD_CHOICE_CHINESE = 'chinese_music_award'

KEY_PRICING_YES_CMTANC = 'per_contestant_yes_cmtanc'
KEY_PRICING_NO_CMTANC = 'per_contestant_no_cmtanc'
KEY_PRICING_YES_INTERNATIONAL = 'per_contestant_yes_international'

# Basic retrieval functions
def print_data():
  pprint(data)

def get_instrument_category(instrument):
  print(data['instrument_categories'][instrument])

def get_instrument_category_age_rules(instrument):
  return dict( (data['age_group_names'][index], age) for index, age in enumerate(data['instrument_categories'][instrument]['age_groups']))

def get_age_measurement_date_epoch():
  return data['age_measurement_cutoff_date']

def get_age_measurement_date():
  return datetime.date.fromtimestamp(data['age_measurement_date'])

def get_instrument_category_choices():
  return map(
    lambda x: str(x),
    data['instrument_categories'].keys()
    )

def get_instrument_category_prices(instrument):
  return data['instrument_categories'][instrument]['pricing']