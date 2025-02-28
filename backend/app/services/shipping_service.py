import aiohttp
import os  # Import os to access environment variables
from ..models.shipping import BookingRequest, TrackingResponse

class ShippingService:
    def __init__(self):
        # Get the API key from environment variables
        self.API_KEY = os.getenv("SHIPPING_API_KEY", None)
        self.API_BASE_URL = os.getenv("SHIPPING_API_BASE_URL", None)
        
        # Define headers once in the constructor
        self.headers = {
            "Authorization": f"ShippoToken {self.API_KEY}",
            "Content-Type": "application/json"
        }
        
    async def create_booking(self, booking_request: BookingRequest = None):
        shipment_data = await self._create_shipment(booking_request)
        rate_id = self._extract_rate_id(shipment_data)
        transaction_data = await self._create_transaction(rate_id)
        return transaction_data

    async def _create_shipment(self, booking_request: BookingRequest):
        async with aiohttp.ClientSession() as session:
            payload = booking_request.dict()
            async with session.post(
                f"{self.API_BASE_URL}/shipments",
                headers=self.headers,
                json=payload
            ) as response:
                return await response.json()

    def _extract_rate_id(self, shipment_data):
        # Extract the rate object_id from the first rate in the rates array
        return shipment_data.get("rates", [])[0].get("object_id") if shipment_data.get("rates") else None

    async def _create_transaction(self, rate_id):
        async with aiohttp.ClientSession() as session:
            transaction_payload = {
                "rate": rate_id,
                "async": False,
            }
            async with session.post(
                f"{self.API_BASE_URL}/transactions",
                headers=self.headers,
                json=transaction_payload
            ) as response:
                return await response.json()

    async def track_shipment(self, tracking_number: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.API_BASE_URL}/tracking/{tracking_number}",
                headers=self.headers
            ) as response:
                data = await response.json()
                return TrackingResponse(**data) 