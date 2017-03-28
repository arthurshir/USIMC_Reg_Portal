$(document).ready(function(){
  $(function() {
      $('.competitor-form').formset({
          prefix: 'ensemble_member',
          formCssClass: 'dynamic-formset2'
      });

      $('.piece-form').formset({
          prefix: 'pieces',
          formCssClass: 'dynamic-formset1'
      });
  })
});

// Client-side form validation using Parsley.js
$(function () {
  $('#application-form').parsley().on('field:validated', function() {
    var ok = $('.parsley-error').length === 0;
    $('.bs-callout-info').toggleClass('hidden', !ok);
    $('.bs-callout-warning').toggleClass('hidden', ok);
  });
});