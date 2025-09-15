// src/Header.js

import React from 'react';
import './Header.css';

function Header() {
  return (
    <div>
      <div className="header">
        <h1>KISAN RAJ</h1>
      </div>
      <div className="topnav">
        <a className="active" href="index.html">
          Home
        </a>
        <a href="#news">Stakeholders</a>
        <a href="#contact">Lot items</a>
        <div className="topnav-right">
          <a href="login.html">Login</a>
          <a href="register.html">Register</a>
        </div>
      </div>
    </div>
  );
}

export default Header;
