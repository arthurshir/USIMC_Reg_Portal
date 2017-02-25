webpackHotUpdate(0,{

/***/ 242:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\n/*This file contains very basic styles.*/\n/**\n * Set up a decent box model on the root element\n */\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%; }\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 3.5em;\n  padding-bottom: 0.5em;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: #FAFAFA; }\n\n#react-app {\n  height: 100%; }\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n\n#app {\n  height: 100%; }\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: 0.5em;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  font-size: 12px;\n  padding: 1em;\n  font-weight: 100;\n  display: flex;\n  flex-direction: row-reverse;\n  color: white;\n  align-items: center;\n  background-color: #54577F;\n  z-index: 1; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Footer.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAyB1D,yCAAyC;AAEzC;;GAEG;AAEH;;;;;GAKG;AAEH;;;;EAIE;AAEF;EACE,UAAS;EACT,WAAU;EACV,YAAW;EACX,aAAY,EACb;;AAED;EACE,mBAAkB;EAClB,qCAAoC;EACpC,mBAjCgB;EAkChB,sBAjCmB;EAkCnB,UAAS;EACT,YAAW;EACX,aAAY;EACZ,0BA/CwB,EAgDzB;;AAED;EACE,aAAY,EACb;;AAID;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB;;AAED;EACE,aAAY,EACb;;AC5ED;EACE,gBAAe;EACf,UAAS;EACT,QAAO;EACP,SAAQ;EACR,cDemB;ECdnB,uCAAkC;EAClC,gBAAe;EACf,aAAY;EACZ,iBAAgB;EAChB,cAAa;EACb,4BAA2B;EAC3B,aAAY;EACZ,oBAAmB;EACnB,0BDPwB;ECQxB,WAAU,EACX","file":"Footer.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\n\n/*This file contains very basic styles.*/\n\n/**\n * Set up a decent box model on the root element\n */\n\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\n\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%;\n}\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: $nav-height;\n  padding-bottom: $footer-height;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: $background-color;\n}\n\n#react-app {\n  height: 100%;\n}\n\n$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}\n\n#app {\n  height: 100%;\n}\n\n\n","@import \"../master\";\n\n.footer {\n  position: fixed;\n  bottom: 0;\n  left: 0;\n  right: 0;\n  height: $footer-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  font-size: 12px;\n  padding: 1em;\n  font-weight: 100;\n  display: flex;\n  flex-direction: row-reverse;\n  color: white;\n  align-items: center;\n  background-color: $dark-brand-color;\n  z-index: 1;\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ }),

/***/ 288:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\n/*This file contains very basic styles.*/\n/**\n * Set up a decent box model on the root element\n */\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%; }\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 3.5em;\n  padding-bottom: 0.5em;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: #FAFAFA; }\n\n#react-app {\n  height: 100%; }\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n\n#app {\n  height: 100%; }\n\n.form__field-wrapper {\n  width: 100%;\n  position: relative;\n  padding-top: 1.75em;\n  border-top: 1px solid #EDEDED;\n  border-bottom: 1px solid #EDEDED;\n  background-color: #fff; }\n\n.form__field-wrapper + .form__field-wrapper {\n  border-top: none; }\n\n.form__field-input:focus ~ .form__field-label {\n  color: #666;\n  background-color: #EDEDED; }\n\n.form__field-input:focus {\n  background-color: #EDEDED;\n  color: #333; }\n\n.form__field-label {\n  position: absolute;\n  top: 0;\n  left: 0;\n  width: 100%;\n  padding: 16px;\n  padding-top: 20px;\n  padding-bottom: 0;\n  margin: 0;\n  z-index: 1;\n  font-size: .8em;\n  color: #999;\n  font-weight: 400;\n  user-select: none;\n  cursor: text; }\n\n.form__field-input {\n  position: relative;\n  padding: 1.625em 16px;\n  width: 100%;\n  color: #666;\n  border: none;\n  outline: 0;\n  letter-spacing: 0.05em; }\n\n.form__submit-btn-wrapper {\n  padding: 2em 1em;\n  width: 100%;\n  background-color: #fff;\n  display: flex;\n  justify-content: center; }\n\n.form__submit-btn {\n  border: none;\n  background-color: #fff;\n  border: 1px solid #E9F1F8;\n  padding: 0.5em 1em;\n  border-radius: 3px;\n  background-color: #E9F1F8;\n  color: white;\n  display: block;\n  margin: 0 auto;\n  position: relative; }\n\n.js-form__err-animation {\n  animation: shake 150ms ease-in-out; }\n\n.form__error-wrapper {\n  display: none;\n  justify-content: center;\n  max-width: calc(100% - 2em);\n  margin: 0 auto;\n  margin-bottom: 1em; }\n\n.form__error {\n  display: none;\n  background-color: #FB4F4F;\n  color: white;\n  margin: 0;\n  padding: 0.5em 1em;\n  font-size: 0.8em;\n  font-family: \"Helvetica Neue Light\", \"Helvetica Neue\", \"Helvetica\", \"Arial\", sans-serif;\n  user-select: none; }\n\n.js-form__err .form__error-wrapper {\n  display: flex; }\n\n.js-form__err--user-doesnt-exist .form__error--username-not-registered,\n.js-form__err--username-exists .form__error--username-taken,\n.js-form__err--password-wrong .form__error--wrong-password,\n.js-form__err--field-missing .form__error--field-missing {\n  display: inline-block; }\n\n@keyframes shake {\n  0% {\n    transform: translateX(0); }\n  25% {\n    transform: translateX(10px); }\n  75% {\n    transform: translateX(-10px); }\n  100% {\n    transform: translateX(0); } }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Form.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAyB1D,yCAAyC;AAEzC;;GAEG;AAEH;;;;;GAKG;AAEH;;;;EAIE;AAEF;EACE,UAAS;EACT,WAAU;EACV,YAAW;EACX,aAAY,EACb;;AAED;EACE,mBAAkB;EAClB,qCAAoC;EACpC,mBAjCgB;EAkChB,sBAjCmB;EAkCnB,UAAS;EACT,YAAW;EACX,aAAY;EACZ,0BA/CwB,EAgDzB;;AAED;EACE,aAAY,EACb;;AAID;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB;;AAED;EACE,aAAY,EACb;;AC5ED;EACE,YAAW;EACX,mBAAkB;EAClB,oBAAmB;EACnB,8BDOuB;ECNvB,iCDMuB;ECLvB,uBAAsB,EACvB;;AAED;EACE,iBAAgB,EACjB;;AAED;EACE,YDAc;ECCd,0BDJuB,ECKxB;;AAED;EACE,0BDRuB;ECSvB,YDLmB,ECMpB;;AAED;EACE,mBAAkB;EAClB,OAAM;EACN,QAAO;EACP,YAAW;EACX,cAAa;EACb,kBAAiB;EACjB,kBAAiB;EACjB,UAAS;EACT,WAAU;EACV,gBAAe;EACf,YDrBa;ECsBb,iBAAgB;EAChB,kBAAiB;EACjB,aAAY,EACb;;AAED;EACE,mBAAkB;EAClB,sBAAqB;EACrB,YAAW;EACX,YD9Bc;EC+Bd,aAAY;EACZ,WAAU;EACV,uBAAsB,EACvB;;AAED;EACE,iBAAgB;EAChB,YAAW;EACX,uBAAsB;EACtB,cAAa;EACb,wBAAuB,EACxB;;AAED;EACE,aAAY;EACZ,uBAAsB;EACtB,0BDvDmB;ECwDnB,mBAAkB;EAClB,mBAAkB;EAClB,0BD1DmB;EC2DnB,aAAY;EACZ,eAAc;EACd,eAAc;EACd,mBAAkB,EACnB;;AAED;EACE,mCAAkC,EACnC;;AAED;EACE,cAAa;EACb,wBAAuB;EACvB,4BAA2B;EAC3B,eAAc;EACd,mBAAkB,EACnB;;AAED;EACE,cAAa;EACb,0BD7EmB;EC8EnB,aAAY;EACZ,UAAS;EACT,mBAAkB;EAClB,iBAAgB;EAChB,wFDxF0F;ECyF1F,kBAAiB,EAClB;;AAED;EACE,cAAa,EACd;;AAED;;;;EAIE,sBAAqB,EACtB;;AAED;EACE;IACE,yBAAwB,EAAA;EAE1B;IACE,4BAA2B,EAAA;EAE7B;IACE,6BAA4B,EAAA;EAE9B;IACE,yBAAwB,EAAA,EAAA","file":"Form.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\n\n/*This file contains very basic styles.*/\n\n/**\n * Set up a decent box model on the root element\n */\n\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\n\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%;\n}\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: $nav-height;\n  padding-bottom: $footer-height;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: $background-color;\n}\n\n#react-app {\n  height: 100%;\n}\n\n$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}\n\n#app {\n  height: 100%;\n}\n\n\n","@import \"../master\";\n\n.form__field-wrapper {\n  width: 100%;\n  position: relative;\n  padding-top: 1.75em;\n  border-top: 1px solid $very-light-grey;\n  border-bottom: 1px solid $very-light-grey;\n  background-color: #fff;\n}\n\n.form__field-wrapper + .form__field-wrapper {\n  border-top: none;\n}\n\n.form__field-input:focus ~ .form__field-label {\n  color: $dark-grey;\n  background-color: $very-light-grey;\n}\n\n.form__field-input:focus {\n  background-color: $very-light-grey;\n  color: $very-dark-grey;\n}\n\n.form__field-label {\n  position: absolute;\n  top: 0;\n  left: 0;\n  width: 100%;\n  padding: 16px;\n  padding-top: 20px;\n  padding-bottom: 0;\n  margin: 0;\n  z-index: 1;\n  font-size: .8em;\n  color: $mid-grey;\n  font-weight: 400;\n  user-select: none;\n  cursor: text;\n}\n\n.form__field-input {\n  position: relative;\n  padding: 1.625em 16px;\n  width: 100%;\n  color: $dark-grey;\n  border: none;\n  outline: 0;\n  letter-spacing: 0.05em;\n}\n\n.form__submit-btn-wrapper {\n  padding: 2em 1em;\n  width: 100%;\n  background-color: #fff;\n  display: flex;\n  justify-content: center;\n}\n\n.form__submit-btn {\n  border: none;\n  background-color: #fff;\n  border: 1px solid $brand-color;\n  padding: 0.5em 1em;\n  border-radius: 3px;\n  background-color: $brand-color;\n  color: white;\n  display: block;\n  margin: 0 auto;\n  position: relative;\n}\n\n.js-form__err-animation {\n  animation: shake 150ms ease-in-out;\n}\n\n.form__error-wrapper {\n  display: none;\n  justify-content: center;\n  max-width: calc(100% - 2em);\n  margin: 0 auto;\n  margin-bottom: 1em;\n}\n\n.form__error {\n  display: none;\n  background-color: $error-color;\n  color: white;\n  margin: 0;\n  padding: 0.5em 1em;\n  font-size: 0.8em;\n  font-family: $text-font-stack;\n  user-select: none;\n}\n\n.js-form__err .form__error-wrapper {\n  display: flex;\n}\n\n.js-form__err--user-doesnt-exist .form__error--username-not-registered,\n.js-form__err--username-exists .form__error--username-taken,\n.js-form__err--password-wrong .form__error--wrong-password,\n.js-form__err--field-missing .form__error--field-missing {\n  display: inline-block;\n}\n\n@keyframes shake {\n  0% {\n    transform: translateX(0);\n  }\n  25% {\n    transform: translateX(10px);\n  }\n  75% {\n    transform: translateX(-10px);\n  }\n  100% {\n    transform: translateX(0);\n  }\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ }),

/***/ 290:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\n/*This file contains very basic styles.*/\n/**\n * Set up a decent box model on the root element\n */\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%; }\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 3.5em;\n  padding-bottom: 0.5em;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: #FAFAFA; }\n\n#react-app {\n  height: 100%; }\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n\n#app {\n  height: 100%; }\n\n.form-page__wrapper {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  height: 100%;\n  width: 100%; }\n\n.form-page__form-wrapper {\n  max-width: 325px;\n  width: 100%;\n  border: 1px solid #EDEDED;\n  border-radius: 3px;\n  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);\n  background-color: #fff; }\n\n.form-page__form-heading {\n  text-align: center;\n  font-size: 1em;\n  user-select: none; }\n\n.form-page__form-header {\n  padding: 1em; }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/FormPage.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAyB1D,yCAAyC;AAEzC;;GAEG;AAEH;;;;;GAKG;AAEH;;;;EAIE;AAEF;EACE,UAAS;EACT,WAAU;EACV,YAAW;EACX,aAAY,EACb;;AAED;EACE,mBAAkB;EAClB,qCAAoC;EACpC,mBAjCgB;EAkChB,sBAjCmB;EAkCnB,UAAS;EACT,YAAW;EACX,aAAY;EACZ,0BA/CwB,EAgDzB;;AAED;EACE,aAAY,EACb;;AAID;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB;;AAED;EACE,aAAY,EACb;;AC5ED;EACE,cAAa;EACb,oBAAmB;EACnB,wBAAuB;EACvB,aAAY;EACZ,YAAW,EACZ;;AAED;EACE,iBAAgB;EAChB,YAAW;EACX,0BDAuB;ECCvB,mBAAkB;EAClB,4CAA2C;EAC3C,uBAAsB,EACvB;;AAED;EACE,mBAAkB;EAClB,eAAc;EACd,kBAAiB,EAClB;;AAED;EACE,aAAY,EACb","file":"FormPage.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\n\n/*This file contains very basic styles.*/\n\n/**\n * Set up a decent box model on the root element\n */\n\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\n\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%;\n}\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: $nav-height;\n  padding-bottom: $footer-height;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: $background-color;\n}\n\n#react-app {\n  height: 100%;\n}\n\n$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}\n\n#app {\n  height: 100%;\n}\n\n\n","@import \"../master\";\n\n.form-page__wrapper {\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  height: 100%;\n  width: 100%;\n}\n\n.form-page__form-wrapper {\n  max-width: 325px;\n  width: 100%;\n  border: 1px solid $very-light-grey;\n  border-radius: 3px;\n  box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);\n  background-color: #fff;\n}\n\n.form-page__form-heading {\n  text-align: center;\n  font-size: 1em;\n  user-select: none;\n}\n\n.form-page__form-header {\n  padding: 1em;\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ }),

/***/ 42:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\n/*This file contains very basic styles.*/\n/**\n * Set up a decent box model on the root element\n */\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%; }\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: 3.5em;\n  padding-bottom: 0.5em;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: #FAFAFA; }\n\n#react-app {\n  height: 100%; }\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 16px; }\n\n#app {\n  height: 100%; }\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 3.5em;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: #E9F1F8;\n  z-index: 1; }\n  .nav .nav__wrapper {\n    /*max-width: $max-width;*/\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex; }\n    .nav .nav__wrapper .nav__logo-wrapper {\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none; }\n      .nav .nav__wrapper .nav__logo-wrapper:active {\n        color: inherit; }\n      .nav .nav__wrapper .nav__logo-wrapper #logo {\n        width: 50px;\n        height: 50px;\n        margin: 5px; }\n      .nav .nav__wrapper .nav__logo-wrapper .title {\n        margin: 5px;\n        height: 55px;\n        display: flex;\n        flex-direction: column;\n        justify-content: center; }\n        .nav .nav__wrapper .nav__logo-wrapper .title #title-text {\n          line-height: 26px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 22px;\n          flex: 1;\n          color: #000000;\n          letter-spacing: -0.06px;\n          /* Just so it's visible */ }\n        .nav .nav__wrapper .nav__logo-wrapper .title #sub-text {\n          line-height: 18px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 15px;\n          letter-spacing: -0.07px; }\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase; }\n\n.btn--nav + .btn--nav {\n  margin-left: 1em; }\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none; }\n  .nav__logo-wrapper {\n    margin: 0 auto; }\n  .btn--nav {\n    display: none; } }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Nav.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAyB1D,yCAAyC;AAEzC;;GAEG;AAEH;;;;;GAKG;AAEH;;;;EAIE;AAEF;EACE,UAAS;EACT,WAAU;EACV,YAAW;EACX,aAAY,EACb;;AAED;EACE,mBAAkB;EAClB,qCAAoC;EACpC,mBAjCgB;EAkChB,sBAjCmB;EAkCnB,UAAS;EACT,YAAW;EACX,aAAY;EACZ,0BA/CwB,EAgDzB;;AAED;EACE,aAAY,EACb;;AAID;EACE,mDAAkD;EAClD,eAAc;EACd,cAAa;EACb,aAAY;EACZ,gBAPoB,EAQrB;;AAED;EACE,aAAY,EACb;;AC5ED;EACE,gBAAe;EACf,OAAM;EACN,QAAO;EACP,SAAQ;EACR,cDcgB;ECbhB,uCAAkC;EAClC,aAAY;EACZ,cAAa;EACb,oBAAmB;EACnB,0BDJmB;ECKnB,WAAU,EAkDX;EA7DD;IAcI,0BAA0B;IAC1B,YAAW;IACX,oBAAmB;IACnB,+BAA8B;IAC9B,eAAc;IACd,cAAa,EAyCd;IA5DH;MAsBM,oBAAmB;MACnB,+BAA8B;MAC9B,cAAa;MACb,sBAAqB,EAkCtB;MA3DL;QA2BQ,eAAc,EACf;MA5BP;QA+BQ,YAAW;QACX,aAAY;QACZ,YAAU,EACX;MAlCP;QAoCQ,YAAW;QACX,aAAY;QACZ,cAAa;QACb,uBAAsB;QACtB,wBAAuB,EAkBxB;QA1DP;UA0CU,kBAAiB;UACjB,YAAW;UACX,iBAAgB;UAChB,gBAAe;UACf,QAAO;UACP,eAAc;UACd,wBAAuB;UACvB,0BAA0B,EAC3B;QAlDT;UAoDU,kBAAiB;UACjB,YAAW;UACX,iBAAgB;UAChB,gBAAe;UACf,wBAAuB,EACxB;;AAMT;EACE,iBAAgB;EAChB,0BAAyB,EAC1B;;AAED;EACE,iBAAgB,EACjB;;AAED;EACE;IACE,sBAAqB,EACtB;EAED;IACE,eAAc,EACf;EAED;IACE,cAAa,EACd,EAAA","file":"Nav.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\n\n/*This file contains very basic styles.*/\n\n/**\n * Set up a decent box model on the root element\n */\n\n/*html {\n  box-sizing: border-box;\n}\n*, *::before, *::after {\n  box-sizing: inherit;\n}*/\n\n/*\n#react-app{\n  align-items: stretch;\n  }\n*/\n\nhtml {\n  margin: 0;\n  padding: 0;\n  width: 100%;\n  height: 100%;\n}\n\nbody {\n  position: absolute;\n  font-family: 'Fira Sans', sans-serif;\n  padding-top: $nav-height;\n  padding-bottom: $footer-height;\n  margin: 0;\n  width: 100%;\n  height: 100%;\n  background-color: $background-color;\n}\n\n#react-app {\n  height: 100%;\n}\n\n$wrapper-padding: 16px;\n\n.wrapper {\n  max-width: calc($max-width + $wrapper-padding * 2);\n  margin: 0 auto;\n  display: flex;\n  height: 100%;\n  padding: 0 $wrapper-padding;\n}\n\n#app {\n  height: 100%;\n}\n\n\n","@import \"../master\";\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: $nav-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: $brand-color;\n  z-index: 1;\n\n  .nav__wrapper {\n    /*max-width: $max-width;*/\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex;\n\n    .nav__logo-wrapper {\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none;\n      &:active {\n        color: inherit;\n      }\n\n      #logo {\n        width: 50px;\n        height: 50px;\n        margin:5px;\n      }\n      .title {\n        margin: 5px;\n        height: 55px;\n        display: flex;\n        flex-direction: column;\n        justify-content: center;\n        #title-text {\n          line-height: 26px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 22px;\n          flex: 1;\n          color: #000000;\n          letter-spacing: -0.06px;\n          /* Just so it's visible */\n        }\n        #sub-text {\n          line-height: 18px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 15px;\n          letter-spacing: -0.07px;\n        }\n      }\n    }\n  }\n}\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase;\n}\n\n.btn--nav + .btn--nav {\n  margin-left: 1em;\n}\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none;\n  }\n\n  .nav__logo-wrapper {\n    margin: 0 auto;\n  }\n\n  .btn--nav {\n    display: none;\n  }\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ })

})