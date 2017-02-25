webpackHotUpdate(0,{

/***/ 286:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__constants_AppConstants__ = __webpack_require__(287);
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
const assign = __webpack_require__(4);
// const assign = Object.assign || require('object.assign');

// The initial application state
const initialState = {
  formState: {
    username: '',
    password: ''
  },
  currentlySending: false,
  loggedIn: false //auth.loggedIn()
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

/***/ })

})