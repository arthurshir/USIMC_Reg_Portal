import json
import os
from pprint import pprint
import string
import datetime

# Define folder paths
folder_path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(folder_path, 'rules/data.json')

# Save data
with open(json_path) as json_data:
    data = json.load(json_data)

# Define Constants
RAW_JSON = data

def get_cmtanc_codes():
  return data['cmtanc_codes']