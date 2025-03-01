import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import BookingPage from './pages/Booking/BookingPage';
import TrackingPage from './pages/Tracking/TrackingPage';
import CalendarPage from './pages/Calendar/CalendarPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app">
        <nav className="navbar">
          <div className="nav-brand">Logistics Service</div>
          <ul className="nav-links">
            <li>
              <Link to="/booking">Book Shipment</Link>
            </li>
            <li>
              <Link to="/tracking">Track Shipment</Link>
            </li>
            <li>
              <Link to="/calendar">Calendar</Link>
            </li>
          </ul>
        </nav>

        <main className="main-content">
          <Routes>
            <Route path="/" element={<BookingPage />} />
            <Route path="/booking" element={<BookingPage />} />
            <Route path="/tracking" element={<TrackingPage />} />
            <Route path="/calendar" element={<CalendarPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;