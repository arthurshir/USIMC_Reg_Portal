$(document).ready(function(){
  $(function() {
      $('#piece-table tbody tr').formset({
          prefix: 'pieces',
          formCssClass: 'dynamic-formset1'
      });
  })
});