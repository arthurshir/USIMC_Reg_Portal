webpackHotUpdate(0,{

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
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6_redux__ = __webpack_require__(277);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_redux_thunk__ = __webpack_require__(285);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7_redux_thunk___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_7_redux_thunk__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__reducers_login_js__ = __webpack_require__(286);










// Creates the Redux reducer with the redux-thunk middleware, which allows us
// to do asynchronous things in the actions
const createStoreWithMiddleware = __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_6_redux__["a" /* applyMiddleware */])(__WEBPACK_IMPORTED_MODULE_7_redux_thunk___default.a)(__WEBPACK_IMPORTED_MODULE_6_redux__["b" /* createStore */]);
const store = createStoreWithMiddleware(__WEBPACK_IMPORTED_MODULE_8__reducers_login_js__["a" /* homeReducer */]);

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

/***/ 286:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
throw new Error("Cannot find module \"../constants/AppConstants\"");
throw new Error("Cannot find module \"../utils/auth\"");
/* harmony export (immutable) */ __webpack_exports__["a"] = homeReducer;
/*
 * The reducer takes care of our data
 * Using actions, we can change our application state
 * To add a new action, add it to the switch statement in the homeReducer function
 *
 * Example:
 * case YOUR_ACTION_CONSTANT:
 *   return assign({}, state, {
 *       stateVariable: action.var
 *   });
 */


// Object.assign is not yet fully supported in all browsers, so we fallback to
// a polyfill
const assign = Object.assign || __webpack_require__(!(function webpackMissingModule() { var e = new Error("Cannot find module \"object.assign\""); e.code = 'MODULE_NOT_FOUND';; throw e; }()));


// The initial application state
const initialState = {
  formState: {
    username: '',
    password: ''
  },
  currentlySending: false,
  loggedIn: __WEBPACK_IMPORTED_MODULE_1__utils_auth___default.a.loggedIn()
};

// Takes care of changing the application state
function homeReducer(state = initialState, action) {
  switch (action.type) {
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["CHANGE_FORM"]:
      return assign({}, state, {
        formState: action.newState
      });
      break;
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["SET_AUTH"]:
      return assign({}, state, {
        loggedIn: action.newState
      });
      break;
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["SENDING_REQUEST"]:
      return assign({}, state, {
        currentlySending: action.sending
      });
      break;
    default:
      return state;
  }
}

/***/ })

})