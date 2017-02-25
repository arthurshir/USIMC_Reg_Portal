/**
 *
 * Nav.react.js
 *
 * This component renders the navigation bar
 *
 */

import React, { Component, Image } from 'react';
import { Link } from 'react-router';
import style from '../../stylesheets/components/Footer.scss';

class Footer extends Component {
  render() {
    return(
      <div className="footer">
        <div className="footer__wrapper">
          © Copyright USIMC 2017
        </div>
      </div>
    );
  }
}

export default Footer;
