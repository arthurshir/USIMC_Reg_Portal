$(document).ready(function() {

  /**** Initial function calls ****/
  // Collect rules
  var rules;
  $.getJSON( "/static/registration_site/rules.json", function( data ) {
    rules = data;
  });
  // Trigger category change
  $('#id_instrument_category').trigger("change");


  /**** Listeners ****/
  // Update valid age and award choices
  $('#id_instrument_category').change(function() {
    var instrument_category = $(this).val();
    if ( rules != null ) {
      /**** Update age rules ****/
      // If not all age groups are valid
      deselect_age_options()
      if ( rules['instrument_categories'][instrument_category]['age_groups'].length < rules['age_group_names'].length) {
        // Disable all
        toggle_all_age_options(false);
        // Enable valid age groups
        for (index in rules['instrument_categories'][instrument_category]['age_groups']) {
          toggle_age_option(rules['age_group_names'][index], true)
        }
      } else {
        toggle_all_age_options(true);
      }

      /**** Update award rules ****/
      deselect_award_options();
      toggle_all_award_options(false);
      var valid_awards = get_valid_awards(instrument_category);
      valid_awards.forEach(function(value) {
        toggle_award_option(value, true);
      })

    }
  });

  /**** Rule retrieval ****/
  function get_valid_awards(instrument_category) {
    if ( rules != null ) {
      return Object.keys(rules['awards'])
        .filter( function(value) { return rules['awards'][value]["eligible_instrument_categories"].includes(instrument_category); })
    }
  }

  /**** Toggle functions ****/
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
  function deselect_age_options() {
    $("select#id_age_category option:selected").removeAttr("selected");
  }

  function toggle_all_award_options(enabled) {
    $("#div_id_awards_applying_for input").map(function() {return $(this).val();}).get().
      forEach( function(option) { 
        if (option) {
          toggle_award_option(option, enabled);
        }
    })
  }
  function toggle_award_option(option, enabled) {
    $('#div_id_awards_applying_for input[value=' + option + ']').prop('disabled',!enabled);
  }
  function deselect_award_options() {
    $("#div_id_awards_applying_for input").removeAttr('checked');
  }


})