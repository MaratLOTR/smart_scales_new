// LoginForm.js

import React from 'react';

const LoginForm = ({ email, handleInputChange, handleAuthClick, error }) => {
  return (
    <div className="LoginContainer">
      <label>
        Введите ваш email:
        <input type="text" value={email} onChange={handleInputChange} />
      </label>
      <div className="button-container">
        <button onClick={handleAuthClick}>
          <svg width="180px" height="60px" viewBox="0 0 180 60" className="border">
            <polyline points="179,1 179,59 1,59 1,1 179,1" className="bg-line" />
            <polyline points="179,1 179,59 1,59 1,1 179,1" className="hl-line" />
          </svg>
          <span>Войти</span>
        </button>
      </div>
      {error && <p className="ErrorMessage">{error}</p>}
    </div>
  );
};

export default LoginForm;
