import React from 'react';

const TrackingView = () => {
  // Sample tracking data
  const trackingData = [
    { id: 1, status: 'In Transit', location: 'New York' },
    { id: 2, status: 'Delivered', location: 'Los Angeles' },
  ];

  return (
    <div>
      <h2>Order Tracking</h2>
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