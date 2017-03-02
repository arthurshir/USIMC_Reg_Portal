webpackHotUpdate(0,{

/***/ 116:
/***/ (function(module, exports) {

/*
	MIT License http://www.opensource.org/licenses/mit-license.php
	Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
module.exports = function() {
	var list = [];

	// return the list of modules as css string
	list.toString = function toString() {
		var result = [];
		for(var i = 0; i < this.length; i++) {
			var item = this[i];
			if(item[2]) {
				result.push("@media " + item[2] + "{" + item[1] + "}");
			} else {
				result.push(item[1]);
			}
		}
		return result.join("");
	};

	// import a list of modules into the list
	list.i = function(modules, mediaQuery) {
		if(typeof modules === "string")
			modules = [[null, modules, ""]];
		var alreadyImportedModules = {};
		for(var i = 0; i < this.length; i++) {
			var id = this[i][0];
			if(typeof id === "number")
				alreadyImportedModules[id] = true;
		}
		for(i = 0; i < modules.length; i++) {
			var item = modules[i];
			// skip already imported module
			// this implementation is not 100% perfect for weird media query combinations
			//  when a module is imported multiple times with different media queries.
			//  I hope this will never occur (Hey this way we have smaller bundles)
			if(typeof item[0] !== "number" || !alreadyImportedModules[item[0]]) {
				if(mediaQuery && !item[2]) {
					item[2] = mediaQuery;
				} else if(mediaQuery) {
					item[2] = "(" + item[2] + ") and (" + mediaQuery + ")";
				}
				list.push(item);
			}
		}
	};
	return list;
};


/***/ }),

/***/ 42:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\nbody {\n  font-family: 'Fira Sans', sans-serif; }\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 3.5em;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: #fff;\n  z-index: 1; }\n  .nav .nav__wrapper {\n    max-width: 768px;\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex; }\n    .nav .nav__wrapper .nav__logo-wrapper {\n      width: 437px;\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none;\n      padding: 5px; }\n      .nav .nav__wrapper .nav__logo-wrapper > div {\n        margin: 5px; }\n      .nav .nav__wrapper .nav__logo-wrapper #logo {\n        width: 50px;\n        height: 50px; }\n      .nav .nav__wrapper .nav__logo-wrapper #title {\n        font-size: 22px;\n        flex: 1;\n        color: #000000;\n        letter-spacing: -0.06px;\n        /* Just so it's visible */ }\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase; }\n\n.btn--nav + .btn--nav {\n  margin-left: 1em; }\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none; }\n  .nav__logo-wrapper {\n    margin: 0 auto; }\n  .btn--nav {\n    display: none; } }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Nav.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAuB1D;EACE,qCAAoC,EACrC;;ACvBD;EACE,gBAAe;EACf,OAAM;EACN,QAAO;EACP,SAAQ;EACR,cDcgB;ECbhB,uCAAkC;EAClC,aAAY;EACZ,cAAa;EACb,oBAAmB;EACnB,uBAAsB;EACtB,WAAU,EAmCX;EA9CD;IAcI,iBDIa;ICHb,YAAW;IACX,oBAAmB;IACnB,+BAA8B;IAC9B,eAAc;IACd,cAAa,EA0Bd;IA7CH;MAsBM,aAAY;MACZ,oBAAmB;MACnB,+BAA8B;MAC9B,cAAa;MACb,sBAAqB;MACrB,aAAW,EAiBZ;MA5CL;QA6BQ,YAAU,EACX;MA9BP;QAiCQ,YAAW;QACX,aAAY,EACb;MAnCP;QAsCQ,gBAAe;QACf,QAAO;QACP,eAAc;QACd,wBAAuB;QACvB,0BAA0B,EAC3B;;AAKP;EACE,iBAAgB;EAChB,0BAAyB,EAC1B;;AAED;EACE,iBAAgB,EACjB;;AAED;EACE;IACE,sBAAqB,EACtB;EAED;IACE,eAAc,EACf;EAED;IACE,cAAa,EACd,EAAA","file":"Nav.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n}","@import \"../master\";\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: $nav-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: #fff;\n  z-index: 1;\n\n  .nav__wrapper {\n    max-width: $max-width;\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex;\n\n    .nav__logo-wrapper {\n      width: 437px;\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none;\n      padding:5px;\n      > div{\n        margin:5px;\n      }\n\n      #logo {\n        width: 50px;\n        height: 50px;\n      }\n\n      #title {\n        font-size: 22px;\n        flex: 1;\n        color: #000000;\n        letter-spacing: -0.06px;\n        /* Just so it's visible */\n      }\n    }\n  }\n}\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase;\n}\n\n.btn--nav + .btn--nav {\n  margin-left: 1em;\n}\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none;\n  }\n\n  .nav__logo-wrapper {\n    margin: 0 auto;\n  }\n\n  .btn--nav {\n    display: none;\n  }\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ })

})