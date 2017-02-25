webpackHotUpdate(0,{

/***/ 132:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react__ = __webpack_require__(4);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_react___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_react__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__stylesheets_components_HomePage_scss__ = __webpack_require__(294);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__stylesheets_components_HomePage_scss___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__stylesheets_components_HomePage_scss__);



const HomePage = () => __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
  'article',
  null,
  __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
    'div',
    null,
    __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
      'section',
      { className: 'text-section' },
      __WEBPACK_IMPORTED_MODULE_0_react___default.a.createElement(
        'h1',
        null,
        'Hello welcome to Home Page'
      )
    )
  )
);

/* harmony default export */ __webpack_exports__["a"] = HomePage;

/***/ }),

/***/ 293:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(291)();
// imports


// module
exports.push([module.i, ".wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/components/HomePage.scss"],"names":[],"mappings":"AAEA;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB","file":"HomePage.scss","sourcesContent":["$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}"],"sourceRoot":"webpack://"}]);

// exports


/***/ }),

/***/ 294:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(293);
if(typeof content === 'string') content = [[module.i, content, '']];
// add the styles to the DOM
var update = __webpack_require__(43)(content, {});
if(content.locals) module.exports = content.locals;
// Hot Module Replacement
if(true) {
	// When the styles change, update the <style> tags
	if(!content.locals) {
		module.hot.accept(293, function() {
			var newContent = __webpack_require__(293);
			if(typeof newContent === 'string') newContent = [[module.i, newContent, '']];
			update(newContent);
		});
	}
	// When the module is disposed, remove the <style> tags
	module.hot.dispose(function() { update(); });
}

/***/ })

})