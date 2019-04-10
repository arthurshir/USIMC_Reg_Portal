// Client-side form validation using Parsley.js
$(document).ready(function(){
  $(".competitor-div").on("click", "a", function(){
    update_pricing();
  });

  $('#application-form').on("change", 'input', function(event){
    $('[name="submit-form"]').attr("disabled",true);
  });

  function update_pricing() {
    $.ajax({
      url: "/registration/application/create_pricing_string/",
      type: "GET", //send it through get method
      data: { 
        num_ensemble_members: $('.competitor-form').length,
        num_awards: $('#entry_info_div [name="num_award_categories"]').val(), 
        pk: $('#entry_info_div [name="pk"]').val(),
        is_not_international: $('[name="lives-in-united-states"]').val(),
      },
      success: function(response) {
        $('#pricing_string span').html(replace_new_line_with_br(response));
      },
      error: function(xhr) {
        //Do Something to handle error
      }
    });
  }

});