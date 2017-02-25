webpackHotUpdate(0,{

/***/ 237:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(228);
throw new Error("Cannot find module \"../css/components/Nav.scss\"");
/**
 *
 * Nav.react.js
 *
 * This component renders the navigation bar
 *
 */





class Nav extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    // Render either the Log In and register buttons, or the logout button
    // based on the current authentication state.
    const navButtons = this.props.loggedIn ? __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      null,
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        __WEBPACK_IMPORTED_MODULE_1_react_router__["d" /* Link */],
        { to: '/dashboard', className: 'btn btn--dash btn--nav' },
        'Dashboard'
      )
    ) : __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      null,
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        __WEBPACK_IMPORTED_MODULE_1_react_router__["d" /* Link */],
        { to: '/register', className: 'btn btn--login btn--nav' },
        'Register'
      ),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        __WEBPACK_IMPORTED_MODULE_1_react_router__["d" /* Link */],
        { to: '/login', className: 'btn btn--login btn--nav' },
        'Login'
      )
    );

    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      { className: 'nav' },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'nav__wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          __WEBPACK_IMPORTED_MODULE_1_react_router__["d" /* Link */],
          { to: '/', className: 'nav__logo-wrapper' },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'h1',
            { className: 'nav__logo' },
            'Login\xA0Flow'
          )
        ),
        navButtons
      )
    );
  }
}

Nav.propTypes = {
  loggedIn: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.bool.isRequired
};

/* harmony default export */ __webpack_exports__["a"] = Nav;

/***/ })

})