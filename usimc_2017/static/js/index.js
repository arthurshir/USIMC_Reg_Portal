import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router';
import HomePage from './components/pages/HomePage.js';
import LoginPage from './components/pages/LoginPage.js';
import App from './components/App.js';


ReactDOM.render(
  <Router history={browserHistory}>
    <Route component={App}>
      <Route path="/" component={HomePage} />
      <Route path="/login" component={LoginPage} />
    </Route>
  </Router>,
  document.getElementById('react-app')
);