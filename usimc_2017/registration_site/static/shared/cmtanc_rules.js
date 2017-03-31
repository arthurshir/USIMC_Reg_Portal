
// Collect rules
var rules;
$.getJSON( "/static/registration_site/rules.json", function( data ) {
  rules = data;
});

// Use the age of the competitor at this date to check if he/she is old enough
function age_measurement_date_epoch() {
  return rules['age_measurement_date']
}

function age_measurement_date() {
  var date = new Date(0);
  date.setUTCSeconds(age_measurement_date_epoch())
  return date;
}

function age_group_names() {
  return rules['age_group_names'];
}

function age_group_names_for_instrument_category(instrument_category) {
  return rules['age_group_names'].slice(0, rules['instrument_categories'][instrument_category]['age_groups'].length - 1);
}

function age_for_instrument_category_and_age_group(instrument_category, age_group_name) {
  var age_group_index = age_group_names().indexOf(age_group_name)
  return rules['instrument_categories'][instrument_category]['age_groups'][age_group_index];
}

function cutoff_birthday_for_instrument_category_and_age_group(instrument_category, age_group_name) {
  var max_age = age_for_instrument_category_and_age_group(instrument_category, age_group_name);
  var date = age_measurement_date();
  date.setFullYear(date.getFullYear() - max_age);
  return date;
}

function validate_birthday_for_instrument_category_and_age_group(birthday, instrument_category, age_group_name) {
  return birthday < cutoff_birthday_for_instrument_category_and_age_group(instrument_category, age_group_name);
}

function pricing_for_instrument_category_for_pricing_type_per_contestant_per_awards(instrument_category, pricing_type) {
  return rules['instrument_categories'][instrument_category]['pricing'][pricing_type];
}

function calculate_pricing(instrument_category, num_awards, num_competitors, pricing_type, is_not_international) {
  var per_contestant_per_award = pricing_for_instrument_category_for_pricing_type_per_contestant_per_awards(instrument_category, pricing_type);
  return per_contestant_per_award*num_awards*num_competitors;
}

// constants
const PRICING_TYPE_YES_CMTANC = "per_contestant_yes_cmtanc";
const PRICING_TYPE_NO_CMTANC = "per_contestant_no_cmtanc";
const PRICING_TYPE_YES_INTERNATIONAL = "per_contestant_yes_international";