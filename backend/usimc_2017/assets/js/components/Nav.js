/**
 *
 * Nav.react.js
 *
 * This component renders the navigation bar
 *
 */

import React, { Component, Image } from 'react';
import { Link } from 'react-router';
import style from '../../stylesheets/components/Nav.scss';
import logoimage from '../../images/brand_symbol.png';

class Nav extends Component {
  render() {
    // Render either the Log In and register buttons, or the logout button
    // based on the current authentication state.
    const navButtons = this.props.loggedIn ? (
        <div>
          <Link to="/dashboard" className="btn btn--dash btn--nav">Dashboard</Link>
        </div>
      ) : (
        <div>
          <Link to="/register" className="btn btn--login btn--nav">Register</Link>
          <Link to="/login" className="btn btn--login btn--nav">Login</Link>
        </div>
      );

    return(
      <div className="nav">
        <div className="nav__wrapper">
          <Link to="/" className="nav__logo-wrapper">
            <img
            id='logo'
            src={logoimage} />
            <div className='title'>
              <div>
                <h3 id='title-text'>California Music Teachers Association</h3>
                <p id='sub-text'>Chinese Music Teachers Association of Northern California</p>
              </div>
            </div>
          </Link>
          { navButtons }
        </div>
      </div>
    );
  }
}

Nav.propTypes = {
  loggedIn: React.PropTypes.bool.isRequired,
}

export default Nav;
