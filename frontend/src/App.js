import './App.css';
import React, { useState } from 'react';
import axios from 'axios';
import PulseTemperaturePressure from './PulseTemperaturePressure';
import Status from './Status';
import WeightFatMuscleComponent from './WeightFatMuscleComponent';
import LoginForm from './LoginForm';


function App() {
  const [email, setEmail] = useState('');
  const [userId, setUserId] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    setEmail(e.target.value);
  };

  const handleAuthClick = async () => {
    try {
      const response = await axios.get(`http://192.168.0.112:8080/users/auth/`, { params: { email } });
      console.log(response)
      if ('user_id' in response.data) {
        const { user_id } = response.data;
        setUserId(user_id);
        setError(null);
      } else {
        setError('Неправильный email');
      }
    } catch (error) {
      console.error('Ошибка при авторизации:', error);
      setError('Ошибка при авторизации. Пожалуйста, попробуйте ещё раз.');
    }
  };

  const handleLogout = () => {
    setUserId(null);
    setEmail('');
    setError(null);
  };

  if (userId) {
    return (
      <div className="App">
        <header className="App-header">
          <div className="HealthStatus">
            <div className="HealthData">
              <PulseTemperaturePressure userId={35} />
            </div>
            <div className="ImageContainer">
              <img src={require("./pngtree-standing-young-man-ready-to-exercise-png-image_7538575.png")} className="App-logo" alt="logo" />
            </div>
            <div className="ConstHealthData">
              <WeightFatMuscleComponent userId={35}/>
            </div>
            <div className="StatusContainer">
              <Status userId={35}/>
            </div>
          </div>
          <div className='LogoutButton'>
          <button onClick={handleLogout}>Выход</button>
          </div>
        </header>
        
      </div>
    );  
  }

  return (
    <div className="LoginPage">
      <LoginForm
        email={email}
        handleInputChange={handleInputChange}
        handleAuthClick={handleAuthClick}
        error={error}
      />
    </div>
  );
}

export default App;