// Client-side form validation using Parsley.js
$(document).ready(function(){
  $('#application-form').parsley().on('field:validated', function() {
    var ok = $('.parsley-error').length === 0;
    $('.bs-callout-info').toggleClass('hidden', !ok);
    $('.bs-callout-warning').toggleClass('hidden', ok);
  });


  $(document).on("click", 'a', function(event){
    $("#application-form").parsley().reset();
  });

  $(".competitor-div").on("click", "a", function(){
    update_pricing();
  });

  function update_pricing() {
    $.ajax({
      url: "/application/create_pricing_string/",
      type: "GET", //send it through get method
      data: { 
        num_ensemble_members: $('.competitor-form').length,
        num_awards: $('#entry_info_div [name="num_award_categories"]').val(), 
        pk: $('#entry_info_div [name="pk"]').val()
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