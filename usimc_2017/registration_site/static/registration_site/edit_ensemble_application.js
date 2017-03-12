$(document).ready(function(){
  $(function() {
      $('#ensemble-member-table tbody tr').formset({
          prefix: 'ensemble_member',
          formCssClass: 'dynamic-formset1'
      });

      $('#piece-table tbody tr').formset({
          prefix: 'pieces',
          formCssClass: 'dynamic-formset1'
      });
  })
});