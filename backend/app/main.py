from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config.standard_response import StandardResponse
from .models.shipping import BookingRequest, TrackingResponse
from .services.shipping_service import ShippingService

# Initialize FastAPI application
app = FastAPI()

# Configure CORS to allow requests from the frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allowed origin
    allow_credentials=True,                  # Allow cookies
    allow_methods=["*"],                     # Allow all HTTP methods
    allow_headers=["*"],                     # Allow all headers
)

# Initialize shipping service instance
shipping_service = ShippingService()

# Endpoint to create a new shipping booking
@app.post("/api/booking")
async def create_booking(booking_request: BookingRequest):
    try:
        # Call shipping service to create booking
        booking_data = await shipping_service.create_booking(booking_request)
        # Return success response with booking data
        return StandardResponse(data=booking_data)
    except Exception as e:
        # Return error response if something goes wrong
        return StandardResponse(status=False, message="Failed to create booking", errors=[str(e)])

# Endpoint to track an existing shipment
@app.get("/api/tracking/{tracking_number}")
async def track_shipment(tracking_number: str):
    try:
        # Call shipping service to get tracking information
        tracking_data = await shipping_service.track_shipment(tracking_number)
        # Return success response with tracking data
        return StandardResponse(data=tracking_data)
    except Exception as e:
        # Return error response if something goes wrong
        return StandardResponse(status=False, message="Failed to track shipment", errors=[str(e)])