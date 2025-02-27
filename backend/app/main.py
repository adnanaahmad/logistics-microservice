from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .services.shipping_service import ShippingService
from .models.shipping import BookingRequest, TrackingRequest

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
        result = await shipping_service.create_booking(booking_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/tracking/{tracking_number}")
async def track_shipment(tracking_number: str):
    try:
        result = await shipping_service.track_shipment(tracking_number)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) 