webpackHotUpdate(0,{

/***/ 140:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(34);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss__ = __webpack_require__(285);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_png__ = __webpack_require__(156);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_png___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_png__);
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
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement('img', {
            id: 'logo',
            src: __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_png___default.a }),
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'div',
            { className: 'title' },
            __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
              'div',
              null,
              __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
                'h3',
                { id: 'title-text' },
                'USIMC 2017 Annual Competition'
              ),
              __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
                'p',
                { id: 'sub-text' },
                'Chinese Music Teachers Association of Northern California'
              )
            )
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