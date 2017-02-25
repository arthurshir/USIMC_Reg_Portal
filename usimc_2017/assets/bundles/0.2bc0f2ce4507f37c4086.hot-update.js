webpackHotUpdate(0,{

/***/ 113:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_redux__ = __webpack_require__(272);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__Form_js__ = __webpack_require__(283);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__LoadingIndicator_js__ = __webpack_require__(282);
/*
 * LoginPage
 *
 * Users login on this page
 * Route: /login
 *
 */






class LoginPage extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    const dispatch = this.props.dispatch;
    const { formState } = this.props.data;
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      { className: 'form-page__wrapper' },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form-page__form-wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'div',
          { className: 'form-page__form-header' },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'h2',
            { className: 'form-page__form-heading' },
            'Login'
          )
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2__Form_js__["a" /* default */], { data: formState, dispatch: dispatch, location: location, history: this.props.history, onSubmit: this._login, btnText: "Login" })
      )
    );
  }

  _login(username, password) {}
}

// Which props do we want to inject, given the global state?
function select(state) {
  return {
    data: state
  };
}

// Wrap the component to inject dispatch and state into it
/* harmony default export */ __webpack_exports__["a"] = __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1_react_redux__["a" /* connect */])(select)(LoginPage);

/***/ }),

/***/ 241:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(114);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_router__ = __webpack_require__(72);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_pages_HomePage_js__ = __webpack_require__(112);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__ = __webpack_require__(113);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__components_App_js__ = __webpack_require__(111);







__WEBPACK_IMPORTED_MODULE_1_react_dom___default.a.render(__WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
  __WEBPACK_IMPORTED_MODULE_2_react_router__["a" /* Router */],
  { history: __WEBPACK_IMPORTED_MODULE_2_react_router__["b" /* browserHistory */] },
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    __WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */],
    { component: __WEBPACK_IMPORTED_MODULE_5__components_App_js__["a" /* default */] },
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_3__components_pages_HomePage_js__["a" /* default */] }),
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/login', component: __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__["a" /* default */] })
  )
), document.getElementById('react-app'));

/***/ }),

/***/ 282:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/**
 * LoadingIndicator.react.js
 *
 * A loading indicator, copied from https://github.com/tobiasahlin/SpinKit
 *
 */



// Since this component doesn't need any state, make it a stateless component
function LoadingIndicator() {
  return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    "div",
    null,
    "Loading",
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      "div",
      { className: "sk-fading-circle" },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle1 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle2 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle3 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle4 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle5 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle6 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle7 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle8 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle9 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle10 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle11 sk-circle" }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement("div", { className: "sk-circle12 sk-circle" })
    )
  );
}

/* harmony default export */ __webpack_exports__["a"] = LoadingIndicator;

/***/ }),

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

/***/ }),

/***/ 284:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__LoadingIndicator_js__ = __webpack_require__(282);
/**
 * LoadingButton.react.js
 *
 * Wraps the loading indicator in a tag with the .btn--loading class
 */




function LoadingButton(props) {
  return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    'a',
    { href: '#', className: props.className + " btn btn--loading", disabled: 'true' },
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_1__LoadingIndicator_js__["a" /* default */], null)
  );
}

/* harmony default export */ __webpack_exports__["a"] = LoadingButton;

/***/ })

})