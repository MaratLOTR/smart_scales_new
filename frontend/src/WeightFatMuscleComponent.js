import React, { useState, useEffect } from 'react';

const WeightFatMuscleComponent = ({ userId }) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://192.168.0.112:8080/users/weight_fat_muscle_mass/?user_id=${userId}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchData();
  }, [userId]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!data) {
    return <div>Loading...</div>;
  }

  const headerValueStyle ={
    fontSize: '1.1em',
    margin: '0',  // убираем внешний отступ
    padding: '5px',  // добавляем внутренний отступ
  }
  const userValueStyle = {
    fontSize: '1em',
    margin: '0',  // убираем внешний отступ
    padding: '5px',  // добавляем внутренний отступ
    textAlign: 'left'
  };

  const standardValueStyle = {
    fontSize: '0.8em',
    margin: '0',  // убираем внешний отступ
    padding: '5px',  // добавляем внутренний отступ
    textAlign: 'left'
  };

  return (
    <div>
      <div>
        <h2 style={headerValueStyle}>Вес</h2>
        <p style={userValueStyle}>User: {data.weight.user}</p> 
        <p style={standardValueStyle}>Standard: {data.weight.standard}</p>
        <p style={standardValueStyle}>Description: {data.weight.description}</p>
      </div>
      <div>
        <h2 style={headerValueStyle}>Fat Mass</h2>
        <p style={userValueStyle}>User: {data.fat_mass.user}</p>
        <p style={standardValueStyle}>Standard: {data.fat_mass.standard}</p>
        <p style={standardValueStyle}>Description: {data.fat_mass.description}</p>
      </div>
      <div>
        <h2 style={headerValueStyle}>Muscle Mass</h2>
        <p style={userValueStyle}>User: {data.muscle_mass.user}</p>
        <p style={standardValueStyle}>Standard: {data.muscle_mass.standard}</p>
        <p style={standardValueStyle}>Description: {data.muscle_mass.description}</p>
      </div>
    </div>
  );
};

export default WeightFatMuscleComponent;
