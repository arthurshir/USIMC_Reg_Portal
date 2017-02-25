webpackHotUpdate(0,{

/***/ 123:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(5);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(73);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_redux__ = __webpack_require__(232);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_react_router__ = __webpack_require__(246);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_HomePage_js__ = __webpack_require__(124);






class Dashboard extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      __WEBPACK_IMPORTED_MODULE_3_react_router__["a" /* Router */],
      { history: __WEBPACK_IMPORTED_MODULE_3_react_router__["b" /* browserHistory */] },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_4__components_pages_HomePage_js__["a" /* default */] }),
      '// ',
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        __WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */],
        { onEnter: checkAuth },
        '//   ',
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '/login', component: LoginPage }),
        '//   ',
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '/register', component: RegisterPage }),
        '//   ',
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '/dashboard', component: Dashboard }),
        '// '
      ),
      '// ',
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '*', component: NotFound })
    );
  }
}

// Wrap the component to inject dispatch and state into it
/* harmony default export */ __webpack_exports__["default"] = Dashboard;

/***/ })

})