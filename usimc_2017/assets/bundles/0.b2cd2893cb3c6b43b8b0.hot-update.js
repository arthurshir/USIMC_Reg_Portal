webpackHotUpdate(0,{

/***/ 111:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Nav_js__ = __webpack_require__(115);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Nav_js___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__Nav_js__);
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
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_1__Nav_js__["default"], { history: this.props.history, location: this.props.location }),
      this.props.children
    );
  }
}

// Wrap the component to inject dispatch and state into it
/* harmony default export */ __webpack_exports__["a"] = App;

/***/ }),

/***/ 115:
/***/ (function(module, __webpack_exports__) {

"use strict";
throw new Error("Module build failed: SyntaxError: Expected corresponding JSX closing tag for <p> (38:88)\n\n\u001b[0m \u001b[90m 36 | \u001b[39m            \u001b[33m<\u001b[39m\u001b[33mdiv\u001b[39m className\u001b[33m=\u001b[39m\u001b[32m'title'\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m 37 | \u001b[39m              \u001b[33m<\u001b[39m\u001b[33mh3\u001b[39m id\u001b[33m=\u001b[39m\u001b[32m'title-text'\u001b[39m\u001b[33m>\u001b[39m\u001b[33mCalifornia\u001b[39m \u001b[33mMusic\u001b[39m \u001b[33mTeachers\u001b[39m \u001b[33mAssociation\u001b[39m\u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mh3\u001b[39m\u001b[33m>\u001b[39m\n\u001b[31m\u001b[1m>\u001b[22m\u001b[39m\u001b[90m 38 | \u001b[39m              \u001b[33m<\u001b[39m\u001b[33mp\u001b[39m id\u001b[33m=\u001b[39m\u001b[32m'sub-text'\u001b[39m\u001b[33m>\u001b[39m\u001b[33mChinese\u001b[39m \u001b[33mMusic\u001b[39m \u001b[33mTeachers\u001b[39m \u001b[33mAssociation\u001b[39m of \u001b[33mNorthern\u001b[39m \u001b[33mCalifornia\u001b[39m\u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mh3\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m    | \u001b[39m                                                                                        \u001b[31m\u001b[1m^\u001b[22m\u001b[39m\n \u001b[90m 39 | \u001b[39m            \u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mdiv\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m 40 | \u001b[39m          \u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mLink\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m 41 | \u001b[39m          { navButtons }\u001b[0m\n");

/***/ }),

/***/ 131:
false,

/***/ 239:
false,

/***/ 240:
false,

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

/***/ 42:
false,

/***/ 72:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Router__ = __webpack_require__(215);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return __WEBPACK_IMPORTED_MODULE_0__Router__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Link__ = __webpack_require__(100);
/* unused harmony reexport Link */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__IndexLink__ = __webpack_require__(211);
/* unused harmony reexport IndexLink */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__withRouter__ = __webpack_require__(226);
/* unused harmony reexport withRouter */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__IndexRedirect__ = __webpack_require__(212);
/* unused harmony reexport IndexRedirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__IndexRoute__ = __webpack_require__(213);
/* unused harmony reexport IndexRoute */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__Redirect__ = __webpack_require__(102);
/* unused harmony reexport Redirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__Route__ = __webpack_require__(214);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "c", function() { return __WEBPACK_IMPORTED_MODULE_7__Route__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__RouteUtils__ = __webpack_require__(17);
/* unused harmony reexport createRoutes */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__RouterContext__ = __webpack_require__(66);
/* unused harmony reexport RouterContext */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__PropTypes__ = __webpack_require__(65);
/* unused harmony reexport locationShape */
/* unused harmony reexport routerShape */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__match__ = __webpack_require__(224);
/* unused harmony reexport match */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__useRouterHistory__ = __webpack_require__(107);
/* unused harmony reexport useRouterHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__PatternUtils__ = __webpack_require__(25);
/* unused harmony reexport formatPattern */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__applyRouterMiddleware__ = __webpack_require__(217);
/* unused harmony reexport applyRouterMiddleware */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__browserHistory__ = __webpack_require__(218);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return __WEBPACK_IMPORTED_MODULE_15__browserHistory__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__hashHistory__ = __webpack_require__(222);
/* unused harmony reexport hashHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__createMemoryHistory__ = __webpack_require__(104);
/* unused harmony reexport createMemoryHistory */
/* components */









/* components (configuration) */










/* utils */















/* histories */








/***/ })

})