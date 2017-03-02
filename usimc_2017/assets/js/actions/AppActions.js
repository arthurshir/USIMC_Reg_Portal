import auth from '../utils/auth';
import { SET_AUTH, CHANGE_FORM, SENDING_REQUEST } from '../constants/AppConstants';
import { browserHistory } from 'react-router';

/**
 * Logs an user in
 * @param  {string} username The username of the user to be logged in
 * @param  {string} password The password of the user to be logged in
 */
export function login(username, password) {
  return (dispatch) => {
    // Show the loading indicator, hide the last error
    dispatch(sendingRequest(true));
    // removeLastFormError();
    // If no username or password was specified, throw a field-missing error
    if (anyElementsEmpty({ username, password })) {
      requestFailed({
        type: "field-missing"
      });
      dispatch(sendingRequest(false));
      return;
    }
    // Use auth.js to fake a request
    auth.login(username, password, (success, err) => {
      // When the request is finished, hide the loading indicator
      dispatch(sendingRequest(false));
      dispatch(setAuthState(success));
      if (success === true) {
        // If the login worked, forward the user to the dashboard and clear the form
        forwardTo('/dashboard');
        dispatch(changeForm({
          username: "",
          password: ""
        }));
      } else {
        requestFailed(err);
      }
    });
  }
}

function forwardTo(location) {
  console.log('forwardTo(' + location + ')');
  browserHistory.push(location);
}

/**
 * Sets the authentication state of the application
 * @param {boolean} newState True means a user is logged in, false means no user is logged in
 */
export function setAuthState(newState) {
  return { type: SET_AUTH, newState };
}
