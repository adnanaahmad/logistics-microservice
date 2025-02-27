import aiohttp
from ..models.shipping import BookingRequest, TrackingResponse

class ShippingService:
    def __init__(self):
        # Replace with your actual API credentials
        self.API_KEY = "your_api_key"
        self.API_BASE_URL = "https://api.dhl.com/v1"  # Example using DHL
        
    async def create_booking(self, booking_request: BookingRequest):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "pickup_address": booking_request.pickup_address.dict(),
                "delivery_address": booking_request.delivery_address.dict(),
                "package_details": {
                    "weight": booking_request.package_weight,
                    "dimensions": booking_request.package_dimensions
                },
                "scheduled_date": booking_request.scheduled_date.isoformat()
            }
            
            async with session.post(
                f"{self.API_BASE_URL}/shipments",
                headers=headers,
                json=payload
            ) as response:
                return await response.json()
    
    async def track_shipment(self, tracking_number: str):
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {self.API_KEY}"
            }
            
            async with session.get(
                f"{self.API_BASE_URL}/tracking/{tracking_number}",
                headers=headers
            ) as response:
                data = await response.json()
                return TrackingResponse(**data) 