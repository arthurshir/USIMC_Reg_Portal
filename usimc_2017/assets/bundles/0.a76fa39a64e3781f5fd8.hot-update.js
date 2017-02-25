webpackHotUpdate(0,{

/***/ 42:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(116)();
// imports
exports.push([module.i, "@import url(https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700);", ""]);

// module
exports.push([module.i, "/*This file contains all application-wide CSS variables.*/\nbody {\n  font-family: 'Fira Sans', sans-serif; }\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: 3.5em;\n  box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: #E9F1F8;\n  z-index: 1; }\n  .nav .nav__wrapper {\n    /*max-width: $max-width;*/\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex; }\n    .nav .nav__wrapper .nav__logo-wrapper {\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none; }\n      .nav .nav__wrapper .nav__logo-wrapper:active {\n        color: auto; }\n      .nav .nav__wrapper .nav__logo-wrapper #logo {\n        width: 50px;\n        height: 50px;\n        margin: 5px; }\n      .nav .nav__wrapper .nav__logo-wrapper .title {\n        margin: 5px;\n        height: 55px;\n        display: flex;\n        flex-direction: column;\n        justify-content: center; }\n        .nav .nav__wrapper .nav__logo-wrapper .title #title-text {\n          line-height: 26px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 22px;\n          flex: 1;\n          color: #000000;\n          letter-spacing: -0.06px;\n          /* Just so it's visible */ }\n        .nav .nav__wrapper .nav__logo-wrapper .title #sub-text {\n          line-height: 18px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 15px;\n          letter-spacing: -0.07px; }\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase; }\n\n.btn--nav + .btn--nav {\n  margin-left: 1em; }\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none; }\n  .nav__logo-wrapper {\n    margin: 0 auto; }\n  .btn--nav {\n    display: none; } }\n", "", {"version":3,"sources":["/./assets/stylesheets/components/assets/stylesheets/_master.scss","/./assets/stylesheets/components/assets/stylesheets/components/Nav.scss"],"names":[],"mappings":"AAAA,0DAA0D;AAwB1D;EACE,qCAAoC,EACrC;;ACxBD;EACE,gBAAe;EACf,OAAM;EACN,QAAO;EACP,SAAQ;EACR,cDcgB;ECbhB,uCAAkC;EAClC,aAAY;EACZ,cAAa;EACb,oBAAmB;EACnB,0BDJmB;ECKnB,WAAU,EAkDX;EA7DD;IAcI,0BAA0B;IAC1B,YAAW;IACX,oBAAmB;IACnB,+BAA8B;IAC9B,eAAc;IACd,cAAa,EAyCd;IA5DH;MAsBM,oBAAmB;MACnB,+BAA8B;MAC9B,cAAa;MACb,sBAAqB,EAkCtB;MA3DL;QA2BQ,YAAW,EACZ;MA5BP;QA+BQ,YAAW;QACX,aAAY;QACZ,YAAU,EACX;MAlCP;QAoCQ,YAAW;QACX,aAAY;QACZ,cAAa;QACb,uBAAsB;QACtB,wBAAuB,EAkBxB;QA1DP;UA0CU,kBAAiB;UACjB,YAAW;UACX,iBAAgB;UAChB,gBAAe;UACf,QAAO;UACP,eAAc;UACd,wBAAuB;UACvB,0BAA0B,EAC3B;QAlDT;UAoDU,kBAAiB;UACjB,YAAW;UACX,iBAAgB;UAChB,gBAAe;UACf,wBAAuB,EACxB;;AAMT;EACE,iBAAgB;EAChB,0BAAyB,EAC1B;;AAED;EACE,iBAAgB,EACjB;;AAED;EACE;IACE,sBAAqB,EACtB;EAED;IACE,eAAc,EACf;EAED;IACE,cAAa,EACd,EAAA","file":"Nav.scss","sourcesContent":["/*This file contains all application-wide CSS variables.*/\n\n@import url('https://fonts.googleapis.com/css?family=Fira+Sans:100,300,400,500,600,700');\n\n$text-font-stack: 'Helvetica Neue Light', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;\n$code-font-stack: 'Courier New', 'DejaVu Sans Mono', 'Bitstream Vera Sans Mono', 'Monaco', monospace;\n$serif-font-stack: Georgia, Times, 'Times New Roman', serif;\n\n$brand-color: #E9F1F8;\n$dark-brand-color: #54577F;\n$error-color: #FB4F4F;\n\n$background-color: #FAFAFA;\n$very-light-grey: #EDEDED;\n$light-grey: #CCC;\n$mid-grey: #999;\n$dark-grey: #666;\n$very-dark-grey: #333;\n$text-color: #222;\n\n$max-width: 768px;\n$nav-height: 3.5em;\n$footer-height: 0.5em;\n\nbody {\n  font-family: 'Fira Sans', sans-serif;\n}","@import \"../master\";\n\n.nav {\n  position: fixed;\n  top: 0;\n  left: 0;\n  right: 0;\n  height: $nav-height;\n  box-shadow: 0 0 2px rgba(0,0,0,.5);\n  padding: 1em;\n  display: flex;\n  align-items: center;\n  background-color: $brand-color;\n  z-index: 1;\n\n  .nav__wrapper {\n    /*max-width: $max-width;*/\n    width: 100%;\n    align-items: center;\n    justify-content: space-between;\n    margin: 0 auto;\n    display: flex;\n\n    .nav__logo-wrapper {\n      align-items: center;\n      justify-content: space-between;\n      display: flex;\n      text-decoration: none;\n      &:active {\n        color: auto;\n      }\n\n      #logo {\n        width: 50px;\n        height: 50px;\n        margin:5px;\n      }\n      .title {\n        margin: 5px;\n        height: 55px;\n        display: flex;\n        flex-direction: column;\n        justify-content: center;\n        #title-text {\n          line-height: 26px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 22px;\n          flex: 1;\n          color: #000000;\n          letter-spacing: -0.06px;\n          /* Just so it's visible */\n        }\n        #sub-text {\n          line-height: 18px;\n          margin: 0px;\n          font-weight: 300;\n          font-size: 15px;\n          letter-spacing: -0.07px;\n        }\n      }\n    }\n  }\n}\n\n.btn--nav {\n  font-size: 0.8em;\n  text-transform: uppercase;\n}\n\n.btn--nav + .btn--nav {\n  margin-left: 1em;\n}\n\n@media screen and (max-width: 400px) {\n  .nav__wrapper {\n    justify-content: none;\n  }\n\n  .nav__logo-wrapper {\n    margin: 0 auto;\n  }\n\n  .btn--nav {\n    display: none;\n  }\n}\n"],"sourceRoot":"webpack://"}]);

// exports


/***/ })

})