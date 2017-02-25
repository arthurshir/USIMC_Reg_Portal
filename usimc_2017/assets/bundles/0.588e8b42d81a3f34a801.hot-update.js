webpackHotUpdate(0,{

/***/ 113:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(6);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_react_redux__ = __webpack_require__(272);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__Form_js__ = __webpack_require__(283);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__LoadingIndicator_js__ = __webpack_require__(282);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__stylesheets_components_FormPage_scss__ = __webpack_require__(291);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__stylesheets_components_FormPage_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4__stylesheets_components_FormPage_scss__);
/*
 * LoginPage
 *
 * Users login on this page
 * Route: /login
 *
 */







class LoginPage extends __WEBPACK_IMPORTED_MODULE_0_react__["Component"] {
  render() {
    const dispatch = this.props.dispatch;
    const { formState } = this.props.data;
    return __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'div',
      { className: 'form-page__wrapper' },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'div',
        { className: 'form-page__form-wrapper' },
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
          'div',
          { className: 'form-page__form-header' },
          __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
            'h2',
            { className: 'form-page__form-heading' },
            'Login'
          )
        ),
        __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(__WEBPACK_IMPORTED_MODULE_2__Form_js__["a" /* default */], { data: formState, dispatch: dispatch, location: location, history: this.props.history, onSubmit: this._login, btnText: "Login" })
      )
    );
  }

  _login(username, password) {}
}

// Which props do we want to inject, given the global state?
function select(state) {
  return {
    data: state
  };
}

// Wrap the component to inject dispatch and state into it
/* harmony default export */ __webpack_exports__["a"] = __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_1_react_redux__["b" /* connect */])(select)(LoginPage);

/***/ }),

/***/ 290:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\nbody {\n  font-family: 'Fira Sans', sans-serif; }\n\n.form-page__wrapper {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  height: 100%;\n  width: 100%; }\n\n.form-page__form-wrapper {\n  max-width: 325px;\n  width: 100%;\n  border: 1px solid #EDEDED;\n  border-radius: 3px;\n  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);\n  background-color: #fff; }\n\n.form-page__form-heading {\n  text-align: center;\n  font-size: 1em;\n  user-select: none; }\n\n.form-page__form-header {\n  padding: 1em; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/FormPage.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAwB1D;EACE,qCAAoC,EACrC;;ACxBD;EACE,cAAa;EACb,oBAAmB;EACnB,wBAAuB;EACvB,aAAY;EACZ,YAAW,EACZ;;AAED;EACE,iBAAgB;EAChB,YAAW;EACX,0BDAuB;ECCvB,mBAAkB;EAClB,4CAA2C;EAC3C,uBAAsB,EACvB;;AAED;EACE,mBAAkB;EAClB,eAAc;EACd,kBAAiB,EAClB;;AAED;EACE,aAAY,EACb","file":"FormPage.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n}","@import \"../master\";\n\n.form-page__wrapper {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  height: 100%;\n  width: 100%;\n}\n\n.form-page__form-wrapper {\n  max-width: 325px;\n  width: 100%;\n  border: 1px solid $very-light-grey;\n  border-radius: 3px;\n  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);\n  background-color: #fff;\n}\n\n.form-page__form-heading {\n  text-align: center;\n  font-size: 1em;\n  user-select: none;\n}\n\n.form-page__form-header {\n  padding: 1em;\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ }),

/***/ 291:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(290);
if(typeof content === 'string') content = [[module.i, content, '']];
// add the styles to the DOM
var update = __webpack_require__(239)(content, {});
if(content.locals) module.exports = content.locals;
// Hot Module Replacement
if(true) {
	// When the styles change, update the <style> tags
	if(!content.locals) {
		module.hot.accept(290, function() {
			var newContent = __webpack_require__(290);
			if(typeof newContent === 'string') newContent = [[module.i, newContent, '']];
			update(newContent);
		});
	}
	// When the module is disposed, remove the <style> tags
	module.hot.dispose(function() { update(); });
}

/***/ })

})