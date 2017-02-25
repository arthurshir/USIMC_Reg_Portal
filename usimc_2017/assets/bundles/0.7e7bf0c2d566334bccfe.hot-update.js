webpackHotUpdate(0,{

/***/ 178:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(80);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_router__ = __webpack_require__(228);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_pages_HomePage_js__ = __webpack_require__(234);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__ = __webpack_require__(235);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__components_App_js__ = __webpack_require__(236);







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

/***/ 228:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Router__ = __webpack_require__(220);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return __WEBPACK_IMPORTED_MODULE_0__Router__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Link__ = __webpack_require__(200);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "d", function() { return __WEBPACK_IMPORTED_MODULE_1__Link__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__IndexLink__ = __webpack_require__(216);
/* unused harmony reexport IndexLink */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__withRouter__ = __webpack_require__(232);
/* unused harmony reexport withRouter */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__IndexRedirect__ = __webpack_require__(217);
/* unused harmony reexport IndexRedirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__IndexRoute__ = __webpack_require__(218);
/* unused harmony reexport IndexRoute */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__Redirect__ = __webpack_require__(202);
/* unused harmony reexport Redirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__Route__ = __webpack_require__(219);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "c", function() { return __WEBPACK_IMPORTED_MODULE_7__Route__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__RouteUtils__ = __webpack_require__(181);
/* unused harmony reexport createRoutes */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__RouterContext__ = __webpack_require__(196);
/* unused harmony reexport RouterContext */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__PropTypes__ = __webpack_require__(195);
/* unused harmony reexport locationShape */
/* unused harmony reexport routerShape */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__match__ = __webpack_require__(230);
/* unused harmony reexport match */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__useRouterHistory__ = __webpack_require__(207);
/* unused harmony reexport useRouterHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__PatternUtils__ = __webpack_require__(184);
/* unused harmony reexport formatPattern */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__applyRouterMiddleware__ = __webpack_require__(222);
/* unused harmony reexport applyRouterMiddleware */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__browserHistory__ = __webpack_require__(223);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return __WEBPACK_IMPORTED_MODULE_15__browserHistory__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__hashHistory__ = __webpack_require__(227);
/* unused harmony reexport hashHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__createMemoryHistory__ = __webpack_require__(204);
/* unused harmony reexport createMemoryHistory */
/* components */









/* components (configuration) */










/* utils */















/* histories */








/***/ }),

/***/ 236:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Nav_js__ = __webpack_require__(237);
/**
 *
 * App.react.js
 *
 * This component is the skeleton around the actual pages, and should only
 * contain code that should be seen on all pages. (e.g. navigation bar)
 */

// Import stuff


// import { connect } from 'react-redux';
// import auth from '../utils/auth';

class App extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      { className: 'wrapper' },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_1__Nav_js__["a" /* default */], { history: this.props.history, location: this.props.location }),
      this.props.children
    );
  }
}

// Wrap the component to inject dispatch and state into it
/* harmony default export */ __webpack_exports__["a"] = App;

/***/ }),

/***/ 237:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(228);
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
  loggedIn: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.bool.isRequired,
  currentlySending: __WEBPACK_IMPORTED_MODULE_0_react___default.a.PropTypes.bool.isRequired
};

/* harmony default export */ __webpack_exports__["a"] = Nav;

/***/ })

})