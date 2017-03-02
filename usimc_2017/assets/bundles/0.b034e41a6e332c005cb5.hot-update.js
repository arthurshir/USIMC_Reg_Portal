webpackHotUpdate(0,{

/***/ 283:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(72);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__LoadingButton_js__ = __webpack_require__(284);
/**
 * Form.react.js
 *
 * The form with a username and a password input field, both of which are
 * controlled via the application state.
 *
 */




// Object.assign is not yet fully supported in all browsers, so we fallback to
// a polyfill
// const assign = Object.assign || require('object.assign');

class LoginForm extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'form',
      { className: 'form', onSubmit: this._onSubmit.bind(this) },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form__error-wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'p',
          { className: 'form__error form__error--username-taken' },
          'Sorry, but this username is already taken.'
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'p',
          { className: 'form__error form__error--username-not-registered' },
          'This username does not exist.'
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'p',
          { className: 'form__error form__error--wrong-password' },
          'Wrong password.'
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'p',
          { className: 'form__error form__error--field-missing' },
          'Please fill out the entire form.'
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'p',
          { className: 'form__error form__error--failed' },
          'Something went wrong, please try again!'
        )
      ),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form__field-wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('input', { className: 'form__field-input', type: 'text', id: 'username', value: this.props.data.username, placeholder: 'frank.underwood', onChange: this._changeUsername.bind(this), autoCorrect: 'off', autoCapitalize: 'off', spellCheck: 'false' }),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'label',
          { className: 'form__field-label', htmlFor: 'username' },
          'Username'
        )
      ),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form__field-wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('input', { className: 'form__field-input', id: 'password', type: 'password', value: this.props.data.password, placeholder: '\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022', onChange: this._changePassword.bind(this) }),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'label',
          { className: 'form__field-label', htmlFor: 'password' },
          'Password'
        )
      ),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form__submit-btn-wrapper' },
        this.props.currentlySending ? __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2__LoadingButton_js__["a" /* default */], null) : __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'button',
          { className: 'form__submit-btn', type: 'submit' },
          this.props.btnText
        )
      )
    );
  }

  // Change the username in the app state
  _changeUsername(evt) {
    var newState = this._mergeWithCurrentState({
      username: evt.target.value
    });

    this._emitChange(newState);
  }

  // Change the password in the app state
  _changePassword(evt) {
    var newState = this._mergeWithCurrentState({
      password: evt.target.value
    });

    this._emitChange(newState);
  }

  // onSubmit call the passed onSubmit function
  _onSubmit(evt) {
    evt.preventDefault();
    this.props.onSubmit(this.props.data.username, this.props.data.password);
  }
}

LoginForm.propTypes = {
  onSubmit: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.func.isRequired,
  btnText: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.string.isRequired,
  data: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.object.isRequired
};

/* harmony default export */ __webpack_exports__["a"] = LoginForm;

/***/ })

})