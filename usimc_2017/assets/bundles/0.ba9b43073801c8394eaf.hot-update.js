webpackHotUpdate(0,{

/***/ 290:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(135);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_react_router__ = __webpack_require__(34);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_pages_HomePage_js__ = __webpack_require__(132);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__ = __webpack_require__(133);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__components_pages_RegisterPage_js__ = __webpack_require__(292);
throw new Error("Cannot find module \"./components/pages/DashboardPage.js\"");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__components_App_js__ = __webpack_require__(131);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8_redux__ = __webpack_require__(80);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9_redux_thunk__ = __webpack_require__(136);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9_redux_thunk___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_9_redux_thunk__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10_react_redux__ = __webpack_require__(44);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__reducers_login_js__ = __webpack_require__(134);













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
      { component: __WEBPACK_IMPORTED_MODULE_7__components_App_js__["a" /* default */] },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_4__components_pages_LoginPage_js__["a" /* default */] }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/register/', component: __WEBPACK_IMPORTED_MODULE_5__components_pages_RegisterPage_js__["a" /* default */] }),
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2_react_router__["c" /* Route */], { path: '/dashboard/', component: __WEBPACK_IMPORTED_MODULE_6__components_pages_DashboardPage_js___default.a })
    )
  )
), document.getElementById('react-app'));

/***/ })

})