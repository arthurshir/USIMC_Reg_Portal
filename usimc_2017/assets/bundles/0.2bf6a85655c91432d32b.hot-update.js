webpackHotUpdate(0,{

/***/ 286:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__ = __webpack_require__(287);
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
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["a" /* CHANGE_FORM */]:
      return assign({}, state, {
        formState: action.newState
      });
      break;
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["b" /* SET_AUTH */]:
      return assign({}, state, {
        loggedIn: action.newState
      });
      break;
    case __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__["c" /* SENDING_REQUEST */]:
      return assign({}, state, {
        currentlySending: action.sending
      });
      break;
    default:
      return state;
  }
}

/***/ }),

/***/ 287:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/*
 * AppConstants
 * These are the variables that determine what our central data store (reducer.js)
 * changes in our state. When you add a new action, you have to add a new constant here
 *
 * Follow this format:
 * export const YOUR_ACTION_CONSTANT = 'YOUR_ACTION_CONSTANT';
 */
const CHANGE_FORM = 'CHANGE_FORM';
/* harmony export (immutable) */ __webpack_exports__["a"] = CHANGE_FORM;

const SET_AUTH = 'SET_AUTH';
/* harmony export (immutable) */ __webpack_exports__["b"] = SET_AUTH;

const SENDING_REQUEST = 'SENDING_REQUEST';
/* harmony export (immutable) */ __webpack_exports__["c"] = SENDING_REQUEST;


/***/ })

})