

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
  return birthday < cutoff_birthday_for_instrument_category_and_age_group(instrument_category, age_group_name)
}
