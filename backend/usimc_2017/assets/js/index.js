import React from 'react'
import ReactDOM from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router';
import HomePage from './components/pages/HomePage.js';
import LoginPage from './components/pages/LoginPage.js';
import RegisterPage from './components/pages/RegisterPage.js';
import DashboardPage from './components/pages/DashboardPage.js';
import App from './components/App.js';
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import { Provider } from 'react-redux';
import { homeReducer } from './reducers/login.js';

// Creates the Redux reducer with the redux-thunk middleware, which allows us
// to do asynchronous things in the actions
const createStoreWithMiddleware = applyMiddleware(thunk)(createStore);
const store = createStoreWithMiddleware(homeReducer);

ReactDOM.render(
  <Provider store={store}>
    <Router history={browserHistory}>
      <Route component={App}>
        <Route path="/" component={LoginPage} />
        <Route path="/register/" component={RegisterPage} />
        <Route path="/dashboard/" component={DashboardPage} />
      </Route>
    </Router>
  </Provider>,
  document.getElementById('react-app')
);