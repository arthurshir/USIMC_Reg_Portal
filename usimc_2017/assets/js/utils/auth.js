import BACKEND_API_URL from '../constants/AppConstants.js';
import 'whatwg-fetch'
import 'js-cookie'

/**
 * Authentication lib
 * @type {Object}
 */

curl -X POST -d "username=roylkingarthur@gmail.com&password=1234" http://localhost:8000/users/login

var auth = {
  /**
   * Logs a user in
   * @param  {string}   username The username of the user
   * @param  {string}   password The password of the user
   * @param  {Function} callback Called after a user was logged in on the remote server
   */
  login(username, password, callback) {
    // If there is a token in the localStorage, the user already is
    // authenticated
    if (this.loggedIn()) {
      callback(true);
      return;
    }

    fetch(BACKEND_API_URL + '/users/login', {
      method: 'POST',
      headers: {
        "X-CSRFToken": Cookies.get('csrftoken'),
        "Accept": "application/json",
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password: password,
      })
    }).then(function(response) {
      // handle HTTP response
    }, function(error) {
      console.log('parsing failed', error);
      callback(false, error);
      return;
    }).then(function(json) {
      console.log('parsed json', json);
      callback(true);
      return;
    }).catch(function(error) {
      console.log('parsing failed', error);
      callback(false, error);
      return;
    });

  },
  /**
   * Logs the current user out
   */
  logout(callback) {
    // request.post('/logout', {}, () => {
    //   callback(true);
    // });
  },
  /**
   * Checks if anybody is logged in
   * @return {boolean} True if there is a logged in user, false if there isn't
   */
  loggedIn() {
    if (!!localStorage.token) {
      this.verifylogin(localStorage.token, callback);
    }
    return !!localStorage.token;
  },
  /**
   * Checks if User Token is still valid
   * @param  {string}   password The password of the user
   * @param  {Function} callback
   */
  verifylogin(token, callback) {
    fetch(BACKEND_API_URL + '/users/login', {
      method: 'POST',
      headers: {
        "X-CSRFToken": Cookies.get('csrftoken'),
        "Accept": "application/json",
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
      })
    }).then(function(response) {
      // handle HTTP response
    }, function(error) {
      console.log('error', error);
      callback(false, error);
      return;
    }).then(function(json) {
      console.log('parsed json', json)
      callback(true);
      return;
    }).catch(function(error) {
      console.log('parsing failed', error)
      callback(false, error);
      return;
    });
  }
  /**
   * Registers a user in the system
   * @param  {string}   username The username of the user
   * @param  {string}   password The password of the user
   * @param  {Function} callback Called after a user was registered on the remote server
   */
  register(username, password, callback) {
    // Post a fake request
    request.post('/register', { username, password }, (response) => {
      // If the user was successfully registered, log them in
      if (response.registered === true) {
        this.login(username, password, callback);
      } else {
        // If there was a problem registering, show the error
        callback(false, response.error);
      }
    });
  },
  onChange() {}
}

module.exports = auth;
