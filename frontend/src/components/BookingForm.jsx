import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import Axios
import './BookingForm.css'; // Import the CSS file

const BookingForm = () => {
  const [orderDetails, setOrderDetails] = useState({
    name: '',
    street1: '',
    city: '',
    state: '',
    zip: '',
    country: '',
    phone: '',
    email: ''
  });

  const successMessage = 'Your order has been placed successfully.';
  const errorMessageOne = 'Sorry, we couldn\'t process your order at this time. Please try again or contact our support team for assistance.';
  const errorMessageTwo = 'Oops! Something went wrong while processing your order. Please try again in a few moments or reach out to our support team if the issue persists.';

  const [errors, setErrors] = useState({});
  const [message, setMessage] = useState('');
  const [trackingNumber, setTrackingNumber] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setOrderDetails({ ...orderDetails, [name]: value });
    setErrors({ ...errors, [name]: false });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    const newErrors = {};
    Object.keys(orderDetails).forEach((key) => {
      if (!orderDetails[key]) {
        newErrors[key] = true;
      }
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      setIsLoading(false);
    } else {
      try {
        const payload = {"address_to": orderDetails};
        const response = await axios.post(`${process.env.REACT_APP_BACKEND_BASE_URL}/api/booking`, payload);
        
        if (response.data.status) {
          setMessage(successMessage);
          setTrackingNumber(response.data.data.tracking_number);
        } else {
          setMessage(errorMessageOne);
          setTrackingNumber('');
        }
      } catch (error) {
        console.error('Error booking order:', error);
        setMessage(errorMessageTwo);
        setTrackingNumber('');
      } finally {
        setIsLoading(false); // Set loading to false after request completes
      }
    }
  };

  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => {
        setMessage('');
      }, 5000); // Hide message after 5 seconds
      return () => clearTimeout(timer); // Cleanup the timer on component unmount or when message changes
    }
  }, [message]);

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h2>Book an Order</h2>
        <label className="required-label">Name *</label>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={orderDetails.name}
          onChange={handleChange}
          className={errors.name ? 'error' : ''}
        />
        <label className="required-label">Street Address *</label>
        <input
          type="text"
          name="street1"
          placeholder="Street Address"
          value={orderDetails.street1}
          onChange={handleChange}
          className={errors.street1 ? 'error' : ''}
        />
        <label className="required-label">City *</label>
        <input
          type="text"
          name="city"
          placeholder="City"
          value={orderDetails.city}
          onChange={handleChange}
          className={errors.city ? 'error' : ''}
        />
        <label className="required-label">State *</label>
        <input
          type="text"
          name="state"
          placeholder="State"
          value={orderDetails.state}
          onChange={handleChange}
          className={errors.state ? 'error' : ''}
        />
        <label className="required-label">ZIP Code *</label>
        <input
          type="text"
          name="zip"
          placeholder="ZIP Code"
          value={orderDetails.zip}
          onChange={handleChange}
          className={errors.zip ? 'error' : ''}
        />
        <label className="required-label">Country *</label>
        <input
          type="text"
          name="country"
          placeholder="Country"
          value={orderDetails.country}
          onChange={handleChange}
          className={errors.country ? 'error' : ''}
        />
        <label className="required-label">Phone *</label>
        <input
          type="text"
          name="phone"
          placeholder="Phone"
          value={orderDetails.phone}
          onChange={handleChange}
          className={errors.phone ? 'error' : ''}
        />
        <label className="required-label">Email *</label>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={orderDetails.email}
          onChange={handleChange}
          className={errors.email ? 'error' : ''}
        />
        <button type="submit" disabled={isLoading} className={isLoading ? 'loading' : ''}>
          {isLoading ? 'Booking...' : 'Book'}
        </button>
      </form>
      
      {message && (
        <div className={`message ${message.includes(successMessage) ? 'success' : 'error'}`}>
          {message}
        </div>
      )}

      {trackingNumber && (
        <div className="tracking-number centered">
          Tracking # {trackingNumber}
        </div>
      )}
    </div>
  );
};

export default BookingForm;