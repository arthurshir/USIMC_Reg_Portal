webpackHotUpdate(0,{

/***/ 115:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(72);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss__ = __webpack_require__(238);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2__stylesheets_components_Nav_scss__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_svg__ = __webpack_require__(241);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_svg___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_svg__);
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
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(Image, {
          style: { width: 50, height: 50 },
          source: __WEBPACK_IMPORTED_MODULE_3__images_brand_symbol_svg__["default"] }),
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

/***/ }),

/***/ 241:
/***/ (function(module, exports) {

throw new Error("Module parse failed: /Users/arthurshir/Documents/Contracting/Ling_Registration_Portal/backend/usimc_2017/assets/images/brand_symbol.svg Unexpected token (1:0)\nYou may need an appropriate loader to handle this file type.\n| <?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n| <svg width=\"55px\" height=\"55px\" viewBox=\"0 0 55 55\" version=\"1.1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n|     <!-- Generator: Sketch 3.8.3 (29802) - http://www.bohemiancoding.com/sketch -->");

/***/ })

})