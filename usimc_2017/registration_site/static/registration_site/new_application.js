$(document).ready(function() {
  // Collect rules
  var rules;
  $.getJSON( "/static/registration_site/rules.json", function( data ) {
    rules = data;
    console.log(rules);
  });

  // When instrument is chosen, set available options accordingly
  $('#id_instrument_category').change(function() {
    if ( rules != null && rules['instrument_categories'][$(this).val()]['age_groups'].length < rules['age_group_names'].length) {
      // Disable all
      toggle_all_age_options(false);
      // Toggle 
      for (index in rules['instrument_categories'][$(this).val()]['age_groups']) {
        toggle_age_option(rules['age_group_names'][index], true)
      }
    } else {
      toggle_all_age_options(true);
    }
  });

  function toggle_all_age_options(enabled) {
    $("select#id_age_category option").map(function() {return $(this).val();}).get().
      forEach( function(option) { 
        if (option) {
          toggle_age_option(option, enabled);
        }
    })
  }

  function toggle_age_option(option, enabled) {
    $('select#id_age_category option[value=' + option + ']').prop('disabled',!enabled);
  }
})