webpackHotUpdate(0,{

/***/ 234:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
// /*
//  * HomePage
//  *
//  * This is the first thing users see of the app
//  * Route: /
//  *
//  */

const HomePage = () => React.createElement(
  "article",
  null,
  React.createElement(
    "div",
    null,
    React.createElement(
      "section",
      { className: "text-section" },
      React.createElement(
        "h1",
        null,
        "Hello welcome to Home Page"
      )
    )
  )
);

/* harmony default export */ __webpack_exports__["a"] = HomePage;

/***/ }),

/***/ 79:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(81);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_router__ = __webpack_require__(228);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_pages_HomePage_js__ = __webpack_require__(234);

// import ReactDOM from 'react-dom';
// import { Provider } from 'react-redux';



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
  __WEBPACK_IMPORTED_MODULE_1_react_router__["a" /* Router */],
  { history: __WEBPACK_IMPORTED_MODULE_1_react_router__["b" /* browserHistory */] },
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_1_react_router__["c" /* Route */], { path: '/', component: __WEBPACK_IMPORTED_MODULE_2__components_pages_HomePage_js__["a" /* default */] })
);

/* harmony default export */ __webpack_exports__["a"] = App;

/***/ })

})