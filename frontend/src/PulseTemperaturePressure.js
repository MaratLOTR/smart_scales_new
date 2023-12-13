import React, { useEffect, useState } from 'react';

const PulseTemperaturePressure  = ({ userId }) => {
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
        const response = await fetch(`http://192.168.0.112:8080/users/pulse_pressure_temperature/?user_id=${userId}`);
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
  }, [userId]); // Пустой массив зависимостей означает, что эффект выполняется только после монтирования компонента

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
        <h2 style={headerValueStyle}>Давление</h2>
        <p style={userValueStyle}>User: {healthData.pressure.diastolic_pressure.user}/{healthData.pressure.systolic_pressure.user}</p>
        <p style={standardValueStyle}>Standard: {healthData.pressure.diastolic_pressure.standard}/{healthData.pressure.systolic_pressure.standard}</p>
        <p style={standardValueStyle}>Description: {healthData.pressure.systolic_pressure.description}</p>
      </div>
      <div>
        <h2 style={headerValueStyle}>Пульс</h2>
        <p style={userValueStyle}>User: {healthData.pulse.user}</p>
        <p style={standardValueStyle}>Standard: {healthData.pulse.standard}</p>
        <p style={standardValueStyle}>Description: {healthData.pulse.description}</p>
      </div>
      <div>
        <h2 style={headerValueStyle}>Температура</h2>
        <p style={userValueStyle}>User: {healthData.temperature.user}</p>
        <p style={standardValueStyle}>Standard: {healthData.temperature.standard}</p>
        <p style={standardValueStyle}>Description: {healthData.temperature.description}</p>
      </div>
    </div>
  );
};

export default PulseTemperaturePressure;