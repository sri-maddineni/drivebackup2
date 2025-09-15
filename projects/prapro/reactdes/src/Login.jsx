// src/Login.js

import React from 'react';
import 

function Login() {
  return (
    <div className="container">
      <h2>Login Form</h2>
      <form action="registration_process.php" method="post">
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" name="username" required />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" required />
        </div>

        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
