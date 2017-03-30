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

  window.Parsley.addValidator('maxFileSize', {
    validateString: function(_value, maxSize, parsleyInstance) {
      if (!window.FormData) {
        // alert('You are making all developpers in the world cringe. Upgrade your browser!');
        return true;
      }
      var files = parsleyInstance.$element[0].files;
      return files.length != 1  || files[0].size <= maxSize * 1000000;
    },
    requirementType: 'integer',
    messages: {
      en: 'This file should not be larger than %s Mb'
    }
  });

});
