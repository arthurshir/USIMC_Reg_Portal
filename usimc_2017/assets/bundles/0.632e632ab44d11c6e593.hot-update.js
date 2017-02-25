webpackHotUpdate(0,{

/***/ 270:
false,

/***/ 80:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(52);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_redux__ = __webpack_require__(243);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_react_router__ = __webpack_require__(257);
throw new Error("Cannot find module \"./components/pages/HomePage.react\"");






class Dashboard extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      __WEBPACK_IMPORTED_MODULE_3_react_router__["a" /* Router */],
      { history: __WEBPACK_IMPORTED_MODULE_3_react_router__["b" /* browserHistory */] },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_3_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_4__components_pages_HomePage_react___default.a }),
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