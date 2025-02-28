import React, { useState } from 'react';
import axios from 'axios'; // Import Axios
import './TrackingView.css'; // Import the new CSS file for tracking view

const TrackingView = () => {
  const [trackingNumber, setTrackingNumber] = useState('');
  const [error, setError] = useState(false);
  const [trackingInfo, setTrackingInfo] = useState(null); // State to store tracking info
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  // Sample tracking data
  const trackingData = [
    { id: 1, status: 'In Transit', location: 'New York' },
    { id: 2, status: 'Delivered', location: 'Los Angeles' },
  ];
  
  const errorMessage = 'Oops! Something went wrong. Please try again in a few moments or reach out to our support team if the issue persists.';

  const formatLocation = (location) => {
    if (!location) return 'Location not available';
    
    const parts = [
      location.city,
      location.state,
      location.zip,
      location.country
    ].filter(Boolean); // Remove any null/undefined values
    
    return parts.join(', ');
  };

  const handleTrackOrder = async () => {
    setIsLoading(true);
    if (trackingNumber.trim() === '') {
      setIsLoading(false);
      setError(true);
    } else {
      setError(false);
      try {
        const response = await axios.get(`${process.env.REACT_APP_BACKEND_BASE_URL}/api/tracking/${trackingNumber}`);
        console.log(response.data);

        if (response.data.status) {
          setTrackingInfo({
            status: response.data.data.tracking_status.status,
            location: formatLocation(response.data.data.tracking_status.location),
            details: response.data.data.tracking_status.status_details
          });
        } else {
          setMessage(errorMessage);
          setTrackingInfo(null);
        }
      } catch (err) {
        console.error('Error fetching tracking data:', err);
        setMessage(errorMessage);
      } finally {
        setIsLoading(false);
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
      <button type="button" onClick={handleTrackOrder} disabled={isLoading} className={isLoading ? 'loading' : ''}>
          {isLoading ? 'Track Order...' : 'Track Order'}
        </button>
      {trackingInfo && (
        <div>
          <h3>Tracking Information</h3>
          <p>Status: {trackingInfo.status}</p>
          <p>Location: {trackingInfo.location}</p>
          <p>Details: {trackingInfo.details}</p>
        </div>
      )}
    </div>
  );
};

export default TrackingView; 