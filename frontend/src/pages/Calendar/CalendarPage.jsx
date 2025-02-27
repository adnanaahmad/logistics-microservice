import React from 'react';
import ShippingCalendar from '../../components/ShippingCalendar';
import './CalendarPage.css';

const CalendarPage = () => {
  return (
    <div className="calendar-page">
      <h1>Calendar</h1>
      <ShippingCalendar />
    </div>
  );
};

export default CalendarPage; 