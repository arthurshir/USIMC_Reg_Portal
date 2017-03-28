// Formset handling
$(document).ready(function(){
  $(function() {
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

  // window.Parsley.addValidator('birthday', {
  //   messages: {
  //     en: 'This string is not the reverse of itself',
  //     fr: "Cette valeur n'est pas l'inverse d'elle même."
  //   },
  //   validate: function(_value, requirement, instance) {
  //     if (requirements[1] == $(requirements[0]).val() && '' == value)
  //         return false;
  //     return true;
  //     console.log(_value);
  //     console.log(requirement);
  //     console.log(instance);
  //     // for(var i = 1; i <= requirement; i++)
  //     //   if (instance.parent.isValid({group: 'block-' + i, force: true}))
  //     //     return true; // One section is filled, this check is valid
  //     // return false; // No section is filled, this validation fails
  //   }
  // });
