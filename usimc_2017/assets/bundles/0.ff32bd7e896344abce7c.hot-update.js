webpackHotUpdate(0,{

/***/ 46:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(35)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\n/*This file contains very basic styles.*/\n/**\n * Set up a decent box model on the root element\n */\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%; }\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 80px;\n  padding-bottom: 32px;\n  margin: 0;\n  width: 100%;\n  height: calc(100% - 80px - 32px);\n  background-color: #FAFAFA;\n  display: flex; }\n\n#react-app {\n  align-items: stretch; }\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n\n#app {\n  height: 100%; }\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: 8px;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  font-size: 12px;\n  padding: 1em;\n  font-weight: 100;\n  display: flex;\n  flex-direction: row-reverse;\n  color: white;\n  align-items: center;\n  background-color: #54577F;\n  z-index: 1; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Footer.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAyB1D,yCAAyC;AAEzC;;GAEG;AAEH;;;;;GAKG;AAEH;;;;EAIE;AAEF;EACE,UAAS;EACT,WAAU;EACV,YAAW;EACX,aAAY,EACb;;AAED;EACE,qCAAoC;EACpC,kBAAiB;EACjB,qBAAoB;EACpB,UAAS;EACT,YAAW;EACX,iCAAgC;EAChC,0BA9CwB;EA+CxB,cAAa,EACd;;AAED;EACE,qBAAoB,EACrB;;AAID;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB;;AAED;EACE,aAAY,EACb;;AC5ED;EACE,gBAAe;EACf,UAAS;EACT,QAAO;EACP,SAAQ;EACR,YDeiB;ECdjB,uCAAkC;EAClC,gBAAe;EACf,aAAY;EACZ,iBAAgB;EAChB,cAAa;EACb,4BAA2B;EAC3B,aAAY;EACZ,oBAAmB;EACnB,0BDPwB;ECQxB,WAAU,EACX","file":"Footer.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 56px;\n$footer-height: 8px;\n\n\n/*This file contains very basic styles.*/\n\n/**\n * Set up a decent box model on the root element\n */\n\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\n\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%;\n}\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 80px;\n  padding-bottom: 32px;\n  margin: 0;\n  width: 100%;\n  height: calc(100% - 80px - 32px);\n  background-color: $background-color;\n  display: flex;\n}\n\n#react-app {\n  align-items: stretch;\n}\n\n$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}\n\n#app {\n  height: 100%;\n}\n\n\n","@import \"../master\";\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: $footer-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  font-size: 12px;\n  padding: 1em;\n  font-weight: 100;\n  display: flex;\n  flex-direction: row-reverse;\n  color: white;\n  align-items: center;\n  background-color: $dark-brand-color;\n  z-index: 1;\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ })

})