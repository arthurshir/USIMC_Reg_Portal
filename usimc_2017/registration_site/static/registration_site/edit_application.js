$(document).ready(function(){
  $(function() {
      $('#performer-table tbody tr').formset({
          prefix: 'performers',
          formCssClass: 'dynamic-formset1'
      });

      $('#piece-table tbody tr').formset({
          prefix: 'pieces',
          formCssClass: 'dynamic-formset1'
      });
  })
});
// $(document).ready(function(){
//   function updateElementIndex(el, prefix, ndx) {
//       var id_regex = new RegExp('(' + prefix + '-\\d+)');
//       var replacement = prefix + '-' + ndx;
//       if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
//       if (el.id) el.id = el.id.replace(id_regex, replacement);
//       if (el.name) el.name = el.name.replace(id_regex, replacement);
//     }

//   function addPieceForm(btn, prefix) {
//       var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
//       var row = $('#piece-form:first').clone(true).get(0);
//       $(row).removeAttr('id').insertAfter($('#piece-form:last')).children('.hidden').removeClass('hidden');
//       $(row).children().not(':last').children().each(function() {
//         updateElementIndex(this, prefix, formCount);
//         $(this).val('');
//       });
//       $(row).find('input:text').val('');
//       $(row).find(".hidden").removeClass('hidden');
//       $(row).find('.delete-piece').click(function() {
//         deletePieceForm(this, prefix);
//       });
//       $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
//       return false;
//   }

//   function deletePieceForm(btn, prefix) {
//       $(btn).parents('tbody').find('input:checkbox:first').attr('checked', 'checked');
//       $(btn).parents('tbody').hide();
//       var forms = $('#piece-form');
//       $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
//       for (var i=0, formCount=forms.length; i<formCount; i++) {
//         $(forms.get(i)).children().not(':last').children().each(function() {
//             updateElementIndex(this, prefix, i);
//         });
//       }
//       return false;
//   }

//   $('.add-piece').click(function() {
//     return addPieceForm(this, 'form');
//   });
//   $('.delete-piece').click(function() {
//     return deletePieceForm(this, 'form');
//   })

//   function addPerformerForm(btn, prefix) {
//       var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
//       var row = $('#performer-form:first').clone(true).get(0);
//       $(row).removeAttr('id').insertAfter($('#performer-form:last')).children('.hidden').removeClass('hidden');
//       $(row).children().not(':last').children().each(function() {
//         updateElementIndex(this, prefix, formCount);
//         $(this).val('');
//       });
//       $(row).find('input:text').val('');
//       $(row).find(".hidden").removeClass('hidden');
//       $(row).find('.delete-performer').click(function() {
//         deletePerformerForm(this, prefix);
//       });
//       $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
//       console.log(formCount + 1);
//       return false;
//   }

//   function deletePerformerForm(btn, prefix) {
//       $(btn).parents('tbody').find('input:checkbox:first').attr('checked', 'checked');
//       $(btn).parents('tbody').hide();
//       var forms = $('#performer-form');
//       $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
//       for (var i=0, formCount=forms.length; i<formCount; i++) {
//         $(forms.get(i)).children().not(':last').children().each(function() {
//             updateElementIndex(this, prefix, i);
//         });
//       }
//       return false;
//   }

//   $('.add-performer').click(function() {
//     return addPerformerForm(this, 'performers');
//   });
//   $('.delete-performer').click(function() {
//     return deletePerformerForm(this, 'performers');
//   })
// })