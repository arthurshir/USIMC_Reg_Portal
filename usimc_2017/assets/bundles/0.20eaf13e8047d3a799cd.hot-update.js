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
    const { formState } = {};
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
/* harmony export (immutable) */ __webpack_exports__["a"] = LoginPage;


/***/ })

})