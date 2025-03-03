import aiohttp
import os
import random
from typing import Optional
from ..models.shipping import BookingRequest, TrackingResponse, ShipmentResponse, TransactionResponse
from ..config.constants import BOOKING_PAYLOAD_TEMPLATE, MOCK_TRACKING_NUMBERS


class ShippingService:
    def __init__(self):
        # Initialize API credentials from environment variables
        self.API_KEY = os.getenv("SHIPPING_API_KEY", None)
        self.API_BASE_URL = os.getenv("SHIPPING_API_BASE_URL", None)
        # Set up headers for API requests
        self.headers = {
            "Authorization": f"ShippoToken {self.API_KEY}",
            "Content-Type": "application/json"
        }
        
    async def create_booking(self, booking_request: BookingRequest = None):
        """Main method to create a shipping booking"""
        # Create shipment and get rate ID
        shipment_data = await self._create_shipment(booking_request)
        rate_id = self._extract_rate_id(shipment_data)
        # Create transaction using the rate ID
        transaction_data = await self._create_transaction(rate_id)
        return transaction_data

    async def _create_shipment(self, booking_request: BookingRequest) -> ShipmentResponse:
        """Create a shipment using the booking payload"""
        async with aiohttp.ClientSession() as session:
            # Combine template payload with request data
            payload = BOOKING_PAYLOAD_TEMPLATE | booking_request.dict()
            async with session.post(
                f"{self.API_BASE_URL}/shipments",
                headers=self.headers,
                json=payload
            ) as response:
                response_data = await response.json()
                return ShipmentResponse(**response_data)

    def _extract_rate_id(self, shipment_data: ShipmentResponse) -> Optional[str]:
        """Extract the rate ID from shipment response"""
        # Access the rates attribute directly
        if shipment_data.rates:
            return shipment_data.rates[0].object_id
        return None

    async def _create_transaction(self, rate_id) -> TransactionResponse:
        """Create a transaction using the rate ID"""
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
                response_data = await response.json()
                return TransactionResponse(**response_data)

    async def track_shipment(self, tracking_number: str):
        """Track a shipment using its tracking number"""
        tracking_data = await self._get_tracking_data(tracking_number)
        return tracking_data

    async def _get_tracking_data(self, tracking_number: str) -> TrackingResponse:
        """Get tracking data from the shipping API"""
        # Use a random mock tracking number for testing
        tracking_number = MOCK_TRACKING_NUMBERS[random.randint(0, 4)]
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.API_BASE_URL}/tracks/shippo/{tracking_number}",
                headers=self.headers
            ) as response:
                data = await response.json()
                return TrackingResponse(**data) 