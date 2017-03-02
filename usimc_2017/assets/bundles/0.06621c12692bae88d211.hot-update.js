webpackHotUpdate(0,{

/***/ 242:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\nbody {\n  font-family: 'Fira Sans', sans-serif; }\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: 1em;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  padding: 1em;\n  display: flex;\n  color: white;\n  align-items: center;\n  background-color: #54577F;\n  z-index: 1; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Footer.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAwB1D;EACE,qCAAoC,EACrC;;ACxBD;EACE,gBAAe;EACf,UAAS;EACT,QAAO;EACP,SAAQ;EACR,YDemB;ECdnB,uCAAkC;EAClC,aAAY;EACZ,cAAa;EACb,aAAY;EACZ,oBAAmB;EACnB,0BDJwB;ECKxB,WAAU,EACX","file":"Footer.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 1.0em;\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n}","@import \"../master\";\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: $footer-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  padding: 1em;\n  display: flex;\n  color: white;\n  align-items: center;\n  background-color: $dark-brand-color;\n  z-index: 1;\n}"],"sourceRoot":"webpack://"}]);

// exports


/***/ })

})