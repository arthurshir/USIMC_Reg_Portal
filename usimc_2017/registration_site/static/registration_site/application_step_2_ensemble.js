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