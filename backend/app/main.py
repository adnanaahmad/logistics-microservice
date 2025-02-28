from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config.standard_response import StandardResponse
from .models.shipping import BookingRequest, TrackingResponse
from .services.shipping_service import ShippingService

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

shipping_service = ShippingService()

@app.post("/api/booking")
async def create_booking(booking_request: BookingRequest):
    try:
        booking_data = await shipping_service.create_booking(booking_request)
        return StandardResponse(data=booking_data)
    except Exception as e:
        return StandardResponse(status=False, message="Failed to create booking", errors=[str(e)])

@app.get("/api/tracking/{tracking_number}")
async def track_shipment(tracking_number: str):
    try:
        tracking_data = await shipping_service.track_shipment(tracking_number)
        return StandardResponse(data=tracking_data)
    except Exception as e:
        return StandardResponse(status=False, message="Failed to track shipment", errors=[str(e)])