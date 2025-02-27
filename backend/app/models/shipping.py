from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    state: str
    postal_code: str
    country: str

class BookingRequest(BaseModel):
    pickup_address: Address
    delivery_address: Address
    package_weight: float
    package_dimensions: dict
    scheduled_date: datetime
    
class TrackingRequest(BaseModel):
    tracking_number: str

class TrackingResponse(BaseModel):
    tracking_number: str
    status: str
    current_location: Optional[dict]
    estimated_delivery: Optional[datetime]
    tracking_history: List[dict] 