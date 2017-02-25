webpackHotUpdate(0,{

/***/ 272:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(52);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/*
 * HomePage
 *
 * This is the first thing users see of the app
 * Route: /
 *
 */



class HomePage extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      "article",
      null,
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        "div",
        null,
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          "section",
          { className: "text-section" },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            "h1",
            null,
            "Hello welcome to Home Page"
          )
        )
      )
    );
  }
}

/* harmony default export */ __webpack_exports__["a"] = HomePage;

/***/ }),

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
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_HomePage_js__ = __webpack_require__(272);






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