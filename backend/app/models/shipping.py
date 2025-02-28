from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Parcel(BaseModel):
    height: float
    distance_unit: str
    length: float
    width: float
    weight: float
    mass_unit: str

class Address(BaseModel):
    name: str
    street1: str
    city: str
    state: str
    zip: str
    country: str
    phone: str
    email: EmailStr

class BookingRequest(BaseModel):
    parcels: List[Parcel]
    address_from: Address
    address_to: Address
    object_purpose: str

class TrackingRequest(BaseModel):
    tracking_number: str

class TrackingResponse(BaseModel):
    tracking_number: str
    status: str
    current_location: Optional[dict]
    estimated_delivery: Optional[datetime]
    tracking_history: List[dict] 