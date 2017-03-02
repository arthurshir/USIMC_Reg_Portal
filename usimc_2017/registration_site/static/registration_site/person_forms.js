$(document).ready(function(){
  function updateElementIndex(el, prefix, ndx) {
      var id_regex = new RegExp('(' + prefix + '-\\d+)');
      var replacement = prefix + '-' + ndx;
      if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
      if (el.id) el.id = el.id.replace(id_regex, replacement);
      if (el.name) el.name = el.name.replace(id_regex, replacement);
    }

  function addForm(btn, prefix) {
      var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
      var row = $('#piece-form:first').clone(true).get(0);
      $(row).removeAttr('id').insertAfter($('#piece-form:last')).children('.hidden').removeClass('hidden');
      $(row).children().not(':last').children().each(function() {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
      });
      $(row).find('.delete-row').click(function() {
        deleteForm(this, prefix);
      });
      $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
      return false;
  }

  function deleteForm(btn, prefix) {
      $(btn).parents('#piece-form').remove();
      var forms = $('#piece-form');
      $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
      for (var i=0, formCount=forms.length; i<formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function() {
            updateElementIndex(this, prefix, i);
        });
      }
      return false;
  }

  $('.add-piece').click(function() {
    return addForm(this, 'form');
  });
  $('.delete-piece').click(function() {
    return deleteForm(this, 'form');
  })
  })