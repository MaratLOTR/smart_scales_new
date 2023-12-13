import React, { useEffect, useState } from 'react';

const HealthStatus = () => {
  const [healthData, setHealthData] = useState({
    pressure: {
      systolic_pressure: {
        user: 0,
        standard: 0,
        description: 'string',
      },
      diastolic_pressure: {
        user: 0,
        standard: 0,
        description: 'string',
      },
    },
    pulse: {
      user: 0,
      standard: 0,
      description: 'string',
    },
    temperature: {
      user: 0,
      standard: 0,
      description: 'string',
    },
    status: {
      health_point: 0,
      description: 'string',
    },
  });

  useEffect(() => {
    const fetchHealthData = async () => {
      try {
        const response = await fetch('http://localhost:8000/users/pulse_pressure_temperature/?user_id=5');
        const data = await response.json();

        setHealthData(data);
      } catch (error) {
        console.error('Ошибка при получении данных:', error);
      }
    };

    // Вызов функции для загрузки данных
    fetchHealthData();

    // Устанавливаем интервал обновления данных каждые 10 секунд
    const intervalId = setInterval(fetchHealthData, 10000);

    // Очистка интервала при размонтировании компонента
    return () => clearInterval(intervalId);
  }, []); // Пустой массив зависимостей означает, что эффект выполняется только после монтирования компонента

  const pulseStyle = {
    color: getColorStyle(healthData.pulse.user, healthData.pulse.standard),
  };

  // Функция для определения цвета в зависимости от условий
  function getColorStyle(userValue, standardValue) {
    const threshold = 0.1; // 10% отклонения
    const difference = Math.abs(userValue - standardValue);

    if (difference === 0) {
      return 'green'; // Зеленый цвет, если значения равны
    } else if (difference / standardValue <= threshold) {
      return 'yellow'; // Желтый цвет, если отклонение не превышает 10%
    } else {
      return 'red'; // Красный цвет в остальных случаях
    }
  }

  return (
    <div className="HealthStatus">
      <div className="HealthData">
        <h1>Давление: {healthData.pressure.systolic_pressure.user}/{healthData.pressure.diastolic_pressure.user}</h1>
        <h1 style={pulseStyle}>Пульс: {healthData.pulse.user}</h1>
        <h1>Температура: {healthData.temperature.user}</h1>
      </div>
      <div className="ImageContainer">
        <img src={require("./pngtree-standing-young-man-ready-to-exercise-png-image_7538575.png")} className="App-logo" alt="logo" />
      </div>
      <div className="StatusContainer">
        <h1>Здоровье: {healthData.status.health_point}</h1>
        <p>{healthData.status.description}</p>
      </div>
    </div>
  );
};

export default HealthStatus;