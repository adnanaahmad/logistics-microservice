import aiohttp
import os
from ..models.shipping import BookingRequest, TrackingResponse, ShipmentResponse, TransactionResponse
from ..config.constants import MOCK_TRACKING_NUMBERS
from typing import Optional

class ShippingService:
    def __init__(self):
        self.API_KEY = os.getenv("SHIPPING_API_KEY", None)
        self.API_BASE_URL = os.getenv("SHIPPING_API_BASE_URL", None)
        self.headers = {
            "Authorization": f"ShippoToken {self.API_KEY}",
            "Content-Type": "application/json"
        }
        
    async def create_booking(self, booking_request: BookingRequest = None):
        shipment_data = await self._create_shipment(booking_request)
        rate_id = self._extract_rate_id(shipment_data)
        transaction_data = await self._create_transaction(rate_id)
        return transaction_data

    async def _create_shipment(self, booking_request: BookingRequest) -> ShipmentResponse:
        async with aiohttp.ClientSession() as session:
            payload = booking_request.dict()
            async with session.post(
                f"{self.API_BASE_URL}/shipments",
                headers=self.headers,
                json=payload
            ) as response:
                response_data = await response.json()
                return ShipmentResponse(**response_data)

    def _extract_rate_id(self, shipment_data: ShipmentResponse) -> Optional[str]:
        # Access the rates attribute directly
        if shipment_data.rates:
            return shipment_data.rates[0].object_id
        return None

    async def _create_transaction(self, rate_id) -> TransactionResponse:
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
        tracking_number = MOCK_TRACKING_NUMBERS[0]
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.API_BASE_URL}/tracks/shippo/{tracking_number}",
                headers=self.headers
            ) as response:
                data = await response.json()
                return TrackingResponse(**data) 