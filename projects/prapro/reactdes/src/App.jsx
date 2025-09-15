import React, { useState } from 'react';
import Header from './Header';
import Login from './Login';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Function to handle login
  const handleLogin = () => {
    setIsLoggedIn(true);
  };

  // Function to handle logout
  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <div>
      <Header
        isLoggedIn={isLoggedIn}
        onLoginClick={handleLogin}
        onLogoutClick={handleLogout}
      />
      {isLoggedIn ? <div>Main Content Here</div> : null}
    </div>
  );
}

export default App;
