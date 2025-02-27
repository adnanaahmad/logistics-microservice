import React, { useState } from 'react';

const BookingForm = () => {
  const [orderDetails, setOrderDetails] = useState({
    name: '',
    address: '',
    date: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setOrderDetails({ ...orderDetails, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic
    console.log('Order booked:', orderDetails);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Book an Order</h2>
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={orderDetails.name}
        onChange={handleChange}
      />
      <input
        type="text"
        name="address"
        placeholder="Address"
        value={orderDetails.address}
        onChange={handleChange}
      />
      <input
        type="date"
        name="date"
        value={orderDetails.date}
        onChange={handleChange}
      />
      <button type="submit">Book</button>
    </form>
  );
};

export default BookingForm; 