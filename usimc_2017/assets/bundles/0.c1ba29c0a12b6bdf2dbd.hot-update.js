webpackHotUpdate(0,{

/***/ 178:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom__ = __webpack_require__(80);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_dom___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_react_dom__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app__ = __webpack_require__(79);




__WEBPACK_IMPORTED_MODULE_1_react_dom___default.a.render(__WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2__app__["a" /* default */], null), document.getElementById('react-app'));

/***/ }),

/***/ 79:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
var _this = this;


// import ReactDOM from 'react-dom';
// import { Provider } from 'react-redux';
// import { Router, Route, IndexRoute, browserHistory } from 'react-router';
// import HomePage from './components/pages/HomePage.js';


// const App = ({ }) => (
//   // <Router history={browserHistory}>
//     // <Route path="/" component={HomePage} />
//     // <Route onEnter={checkAuth}>
//     //   <Route path="/login" component={LoginPage} />
//     //   <Route path="/register" component={RegisterPage} />
//     //   <Route path="/dashboard" component={Dashboard} />
//     // </Route>
//     // <Route path="*" component={NotFound} />
//   // </Router>
//       <div>
//       <section className="text-section">
//         <h1>Hello welcome to Home Page</h1>
//       </section>
//     </div>
// )

const App = () => __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
  "div",
  { className: "shopping-list" },
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    "h1",
    null,
    "Shopping List for ",
    _this.props.name
  ),
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    "ul",
    null,
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      "li",
      null,
      "Instagram"
    ),
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      "li",
      null,
      "WhatsApp"
    ),
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      "li",
      null,
      "Oculus"
    )
  )
);

/* harmony default export */ __webpack_exports__["a"] = App;

/***/ })

})