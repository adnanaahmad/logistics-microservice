import React, { useState } from 'react';
import axios from 'axios'; // Import Axios
import './TrackingView.css'; // Import the new CSS file for tracking view

const TrackingView = () => {
  const [trackingNumber, setTrackingNumber] = useState('');
  const [error, setError] = useState(false);
  const [trackingInfo, setTrackingInfo] = useState(null); // State to store tracking info

  // Sample tracking data
  const trackingData = [
    { id: 1, status: 'In Transit', location: 'New York' },
    { id: 2, status: 'Delivered', location: 'Los Angeles' },
  ];

  const handleTrackOrder = async () => {
    if (trackingNumber.trim() === '') {
      setError(true);
    } else {
      setError(false);
      try {
        const response = await axios.get(`${process.env.REACT_APP_BACKEND_BASE_URL}/api/tracking/${trackingNumber}`);
        console.log(response.data);
        setTrackingInfo(response.data);
      } catch (err) {
        console.error('Error fetching tracking data:', err);
        setError(true);
      }
    }
  };

  return (
    <div className="tracking-container">
      <h2>Order Tracking</h2>
      <label className="required-label">Tracking Number *</label>
      <input
        type="text"
        name="trackingNumber"
        placeholder="Tracking Number"
        value={trackingNumber}
        onChange={(e) => setTrackingNumber(e.target.value)}
        className={error ? 'error' : ''}
      />
      <button type="button" onClick={handleTrackOrder}>Track Order</button>
      {trackingInfo && (
        <div>
          <h3>Tracking Information</h3>
          <p>Status: {trackingInfo.status}</p>
          <p>Location: {trackingInfo.location}</p>
        </div>
      )}
      <ul>
        {trackingData.map((item) => (
          <li key={item.id}>
            Order #{item.id}: {item.status} - {item.location}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TrackingView; 