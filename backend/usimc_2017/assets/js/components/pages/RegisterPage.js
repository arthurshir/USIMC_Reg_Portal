/*
 * LoginPage
 *
 * Users login on this page
 * Route: /login
 *
 */

import React, { Component} from 'react';
import { connect } from 'react-redux';
import Form from '../Form.js';
import LoadingIndicator from '../LoadingIndicator.js';
import style from '../../../stylesheets/components/FormPage.scss';


class RegisterPage extends Component {
  render() {
    const dispatch = this.props.dispatch;
    const { formState } = this.props.data;
    return (
      <div className="form-page__wrapper">
        <div className="form-page__form-wrapper">
          <div className="form-page__form-header">
            <h2 className="form-page__form-heading">Register</h2>
          </div>
          <Form data={formState} dispatch={dispatch} location={location} history={this.props.history} onSubmit={this._login} btnText={"Register"}/>
        </div>
      </div>
    );
  }

  _login(username, password) {
  }
}

// Which props do we want to inject, given the global state?
function select(state) {
  return {
    data: state
  };
}

// Wrap the component to inject dispatch and state into it
export default connect(select)(RegisterPage);

