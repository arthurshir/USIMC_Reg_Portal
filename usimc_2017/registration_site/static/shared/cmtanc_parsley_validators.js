
$(function () {
  // Birthday Validator
  window.Parsley.addValidator('birthday', {
    messages: {
      en: 'This value is required'
    },
    validate: function(value, requirements, instance) {
      console.log(value);
      console.log(requirements);
      console.log(instance);
      if ('' == value || 0 == value)
          return false;
      return true;
      // for(var i = 1; i <= requirement; i++)
      //   if (instance.parent.isValid({group: 'block-' + i, force: true}))
      //     return true; // One section is filled, this check is valid
      // return false; // No section is filled, this validation fails
    }
  });

});
      // mincheck: {
      //   validateMultiple: function validateMultiple(values, requirement) {
      //     return values.length >= requirement;
      //   },
      //   requirementType: 'integer',
      //   priority: 30
      // },