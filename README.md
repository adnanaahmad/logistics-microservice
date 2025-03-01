# Logistics Microservice

This project is a logistics microservice designed to integrate with courier platform APIs (goshippo). It provides endpoints for tracking packages in real-time and booking orders. Additionally, a frontend interface is included to interact with these features, offering a drag-and-drop calendar view for scheduling packages.

## Features

### Backend
- **API Integration:**
  - Integration with courier platform APIs to fetch real-time tracking details and book shipments.
  - Handles API authentication and error handling.

- **Microservice Endpoints:**
  1. **Tracking Endpoint:** Provides real-time location updates for shipments.
  2. **Order Booking Endpoint:** Facilitates the creation of new orders and booking shipments.

- **Containerization:**
  - Backend and Frontend is containerized using Docker.
  - Multi-container management using Docker Compose.

### Frontend
- **Real-Time Tracking:**
  - Displays real-time package locations using data from the backend.
  - User-friendly interface for shipment status updates.

- **Order Booking:**
  - Form-based interface for booking orders with input validation.

- **Drag-and-Drop Calendar:**
  - Weekly calendar view.
  - Packages listed on the right-hand side can be dragged and dropped into calendar slots for scheduling.


## Tech Stack

### Backend
- **Framework:** FastAPI
- **API Integration:** goshippo APIs

### Frontend
- **Framework:** React


### Deployment
- **Containerization:** Docker

## Installation

### Prerequisites
- Docker and Docker Compose installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/adnanaahmad/logistics-microservice.git
   cd logistics-microservice
   ```

2. Set up environment variables:
   - `.env` file is already added to the root directory for backend API keys and configurations.

3. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - Backend: `http://localhost:8000`
   - Frontend: `http://localhost:3000`

## Usage

### Backend Endpoints
1. **Tracking Endpoint:**
   - `GET /api/tracking/{tracking_id}`
   - Returns real-time location updates for the specified shipment.

2. **Order Booking Endpoint:**
   - `POST /api/booking`
   - Accepts order details and books a shipment.

### Frontend
1. **Real-Time Tracking:**
   - Enter the tracking ID to view shipment status.

2. **Order Booking:**
   - Fill out the order form and submit to book a shipment.

3. **Drag-and-Drop Calendar:**
   - Drag packages from the list on the right to the calendar to schedule deliveries.

## Deployment
- The application can be deployed on cloud platforms like AWS, GCP, or Heroku.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
