$(document).ready(function() {

  VIOLA = 'VA' // Not 4, 5
  CELLO = 'CE' // Not 5

  // All not 3, 4, 5
  CHINESE_TRADITIONAL_INSTRUMENTS_ENSEMBLE = 'CNE'
  CHAMBER_ENSEMBLE = 'CHE'
  VOCAL_ENSEMBLE = 'VOE'

  $('#id_instrument_category').change(function() {
      // TODO: Change this to a more easily changed / dynamic
      if (
          ( $(this).val() === 'VA' ) ||
          ( $(this).val() === 'CE' ) ||
          ( $(this).val() === 'CNE' ) ||
          ( $(this).val() === 'CHE' ) ||
          ( $(this).val() === 'VOE' )
        ) {

        // Enable all
        enable_all_age_options();

        // Set specific rules
        if ( $(this).val() === 'VA' ) {
          toggle_age_option("D", false);
          toggle_age_option("E", false);
        } else if ( $(this).val() === 'CE' ) {
          toggle_age_option("E", false);
        } else {
          toggle_age_option("C", false);
          toggle_age_option("D", false);
          toggle_age_option("E", false);
        }
    } else {
      enable_all_age_options();
    }
  });

  function enable_all_age_options() {
    $("select#id_age_category option").map(function() {return $(this).val();}).get().
      forEach( function(option) { 
        if (option) {
          console.log(option);
          toggle_age_option(option, true);
        }
    })
  }

  function toggle_age_option(option, enabled) {
    $('select#id_age_category option[value=' + option + ']').prop('disabled',!enabled);
  }
})