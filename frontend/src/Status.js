import React, { useEffect, useState } from 'react';

const Status = ({ userId }) => {
  const [healthPoint, setHealthPoint] = useState(null);
  const [description, setDescription] = useState(null);

  const fetchHealthData = async () => {
    try {
      const response = await fetch(`http://192.168.0.112:8080/users/pulse_pressure_temperature/?user_id=${userId}`);
      const data = await response.json();

      // Извлечение значения health_point из полученных данных
      const { status: { health_point } } = data;
      const { status: { description } } = data;

      setHealthPoint(health_point);
      setDescription(description);
    } catch (error) {
      console.error('Ошибка при получении данных:', error);
    }
  };

  useEffect(() => {
    // Вызываем fetchHealthData сразу после монтирования компонента
    fetchHealthData();

    // Устанавливаем интервал для выполнения запроса каждые 10 секунд
    const intervalId = setInterval(() => {
      fetchHealthData();
    }, 10000);

    // Очищаем интервал при размонтировании компонента
    return () => clearInterval(intervalId);
  }, [userId]); // Пустой массив зависимостей означает, что эффект выполняется только после монтирования компонента

  let healthImage;
  if (healthPoint < 4) {
    healthImage = require("./red_circle.png");
  } else if (healthPoint >= 4 && healthPoint <= 7) {
    healthImage = require("./yellow_circle.png");
  } else {
    healthImage = require("./green-circle.png");
  }

  return (
    <div>
      <h1>Общая оценка здоровья: {healthPoint} <img src={healthImage} alt="Green Circle" style={{ width: '40px', height: '40px', marginRight: '5px' }} /> </h1>
      <h1>Описание состояния: {description} </h1>
    </div>
  );
};

export default Status;