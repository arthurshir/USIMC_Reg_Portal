webpackHotUpdate(0,{

/***/ 170:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(226);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_router__ = __webpack_require__(57);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_pages_HomePage_js__ = __webpack_require__(180);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__ = __webpack_require__(181);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__components_pages_RegisterPage_js__ = __webpack_require__(182);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__components_pages_DashboardPage_js__ = __webpack_require__(179);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__components_App_js__ = __webpack_require__(175);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__components_App_js___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_7__components_App_js__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_redux__ = __webpack_require__(152);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9_redux_thunk__ = __webpack_require__(333);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9_redux_thunk___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_9_redux_thunk__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10_react_redux__ = __webpack_require__(56);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__reducers_login_js__ = __webpack_require__(184);













// Creates the Redux reducer with the redux-thunk middleware, which allows us
// to do asynchronous things in the actions
const createStoreWithMiddleware = __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_8_redux__["a" /* applyMiddleware */])(__WEBPACK_IMPORTED_MODULE_9_redux_thunk___default.a)(__WEBPACK_IMPORTED_MODULE_8_redux__["b" /* createStore */]);
const store = createStoreWithMiddleware(__WEBPACK_IMPORTED_MODULE_11__reducers_login_js__["a" /* homeReducer */]);

__WEBPACK_IMPORTED_MODULE_1_react_dom___default.a.render(__WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
  __WEBPACK_IMPORTED_MODULE_10_react_redux__["a" /* Provider */],
  { store: store },
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    __WEBPACK_IMPORTED_MODULE_2_react_router__["a" /* Router */],
    { history: __WEBPACK_IMPORTED_MODULE_2_react_router__["b" /* browserHistory */] },
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      __WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */],
      { component: __WEBPACK_IMPORTED_MODULE_7__components_App_js__["default"] },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__["a" /* default */] }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/register/', component: __WEBPACK_IMPORTED_MODULE_5__components_pages_RegisterPage_js__["a" /* default */] }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/dashboard/', component: __WEBPACK_IMPORTED_MODULE_6__components_pages_DashboardPage_js__["a" /* default */] })
    )
  )
), document.getElementById('react-app'));

/***/ }),

/***/ 175:
/***/ (function(module, __webpack_exports__) {

"use strict";
throw new Error("Module build failed: SyntaxError: JSX attributes must only be assigned a non-empty expression (47:82)\n\n\u001b[0m \u001b[90m 45 | \u001b[39m    \u001b[36mreturn\u001b[39m(\n \u001b[90m 46 | \u001b[39m      \u001b[33m<\u001b[39m\u001b[33mdiv\u001b[39m className\u001b[33m=\u001b[39m\u001b[32m\"wrapper\"\u001b[39m\u001b[33m>\u001b[39m\n\u001b[31m\u001b[1m>\u001b[22m\u001b[39m\u001b[90m 47 | \u001b[39m        \u001b[33m<\u001b[39m\u001b[33mNav\u001b[39m history\u001b[33m=\u001b[39m{\u001b[36mthis\u001b[39m\u001b[33m.\u001b[39mprops\u001b[33m.\u001b[39mhistory} location\u001b[33m=\u001b[39m{\u001b[36mthis\u001b[39m\u001b[33m.\u001b[39mprops\u001b[33m.\u001b[39mlocation} loggedin\u001b[33m=\u001b[39m{}\u001b[33m/\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m    | \u001b[39m                                                                                  \u001b[31m\u001b[1m^\u001b[22m\u001b[39m\n \u001b[90m 48 | \u001b[39m        { \u001b[36mthis\u001b[39m\u001b[33m.\u001b[39mprops\u001b[33m.\u001b[39mchildren }\n \u001b[90m 49 | \u001b[39m        \u001b[33m<\u001b[39m\u001b[33mFooter\u001b[39m\u001b[33m/\u001b[39m\u001b[33m>\u001b[39m\n \u001b[90m 50 | \u001b[39m      \u001b[33m<\u001b[39m\u001b[33m/\u001b[39m\u001b[33mdiv\u001b[39m\u001b[33m>\u001b[39m\u001b[0m\n");

/***/ }),

/***/ 176:
false,

/***/ 178:
false,

/***/ 201:
false,

/***/ 366:
false,

/***/ 368:
false,

/***/ 57:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__Router__ = __webpack_require__(310);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return __WEBPACK_IMPORTED_MODULE_0__Router__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__Link__ = __webpack_require__(139);
/* unused harmony reexport Link */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__IndexLink__ = __webpack_require__(306);
/* unused harmony reexport IndexLink */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__withRouter__ = __webpack_require__(321);
/* unused harmony reexport withRouter */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__IndexRedirect__ = __webpack_require__(307);
/* unused harmony reexport IndexRedirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__IndexRoute__ = __webpack_require__(308);
/* unused harmony reexport IndexRoute */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__Redirect__ = __webpack_require__(141);
/* unused harmony reexport Redirect */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__Route__ = __webpack_require__(309);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "c", function() { return __WEBPACK_IMPORTED_MODULE_7__Route__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__RouteUtils__ = __webpack_require__(23);
/* unused harmony reexport createRoutes */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__RouterContext__ = __webpack_require__(91);
/* unused harmony reexport RouterContext */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__PropTypes__ = __webpack_require__(90);
/* unused harmony reexport locationShape */
/* unused harmony reexport routerShape */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__match__ = __webpack_require__(319);
/* unused harmony reexport match */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__useRouterHistory__ = __webpack_require__(146);
/* unused harmony reexport useRouterHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__PatternUtils__ = __webpack_require__(32);
/* unused harmony reexport formatPattern */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__applyRouterMiddleware__ = __webpack_require__(312);
/* unused harmony reexport applyRouterMiddleware */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__browserHistory__ = __webpack_require__(313);
/* harmony reexport (binding) */ __webpack_require__.d(__webpack_exports__, "b", function() { return __WEBPACK_IMPORTED_MODULE_15__browserHistory__["a"]; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__hashHistory__ = __webpack_require__(317);
/* unused harmony reexport hashHistory */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__createMemoryHistory__ = __webpack_require__(143);
/* unused harmony reexport createMemoryHistory */
/* components */









/* components (configuration) */










/* utils */















/* histories */








/***/ }),

/***/ 61:
false,

/***/ 65:
false

})