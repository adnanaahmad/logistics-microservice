from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime

class Parcel(BaseModel):
    object_owner: Optional[str]
    object_state: Optional[str]
    mass_unit: str
    template: Optional[str]
    extra: Optional[Dict]
    metadata: Optional[str]
    test: Optional[bool]
    object_id: Optional[str]
    object_created: Optional[str]
    object_updated: Optional[str]
    length: str
    width: str
    height: str
    distance_unit: str
    weight: str
    line_items: Optional[List]

class Address(BaseModel):
    name: str
    street1: str
    street2: Optional[str]
    street3: Optional[str]
    city: str
    state: str
    zip: str
    country: str
    street_no: Optional[str]
    phone: str
    email: EmailStr
    company: Optional[str]
    is_residential: Optional[bool]
    test: Optional[bool]
    object_id: Optional[str]
    is_complete: Optional[bool]
    validation_results: Optional[Dict]

class BookingRequest(BaseModel):
    address_to: Address
class TrackingRequest(BaseModel):
    tracking_number: str

class ServiceLevel(BaseModel):
    name: str
    token: str

class TrackingStatus(BaseModel):
    status_date: str
    status_details: str
    location: Optional[Dict]
    substatus: Optional[Dict]
    object_created: str
    object_updated: str
    object_id: str
    status: str

class TrackingHistory(BaseModel):
    status_date: str
    status_details: str
    location: Optional[Dict]
    substatus: Optional[Dict]
    object_created: str
    object_updated: str
    object_id: str
    status: str

class TrackingResponse(BaseModel):
    tracking_number: str
    carrier: str
    servicelevel: ServiceLevel
    transaction: Optional[str]
    address_from: Dict[str, str]
    address_to: Dict[str, str]
    eta: str
    original_eta: str
    metadata: str
    test: bool
    tracking_status: TrackingStatus
    tracking_history: List[TrackingHistory]
    messages: List[str]

class Rate(BaseModel):
    object_id: str
    object_created: str
    object_owner: str
    shipment: str
    amount: str
    currency: str
    amount_local: str
    currency_local: str
    attributes: List[str]
    provider: str
    provider_image_75: str
    provider_image_200: str
    arrives_by: Optional[str]
    duration_terms: str
    messages: List
    carrier_account: str
    zone: str
    test: bool
    servicelevel: ServiceLevel
    estimated_days: int
    included_insurance_price: Optional[str]

class ShipmentResponse(BaseModel):
    object_id: str
    object_created: str
    object_updated: str
    object_owner: str
    test: bool
    metadata: str
    messages: List
    extra: Dict
    order: Optional[str]
    carrier_accounts: List
    address_from: Address
    address_to: Address
    parcels: List[Parcel]
    status: str
    shipment_date: str
    address_return: Address
    rates: List[Rate]
    alternate_address_to: Optional[str]
    customs_declaration: Optional[str]

class Message(BaseModel):
    source: str
    code: str
    text: str

class CreatedBy(BaseModel):
    first_name: str
    last_name: str
    username: str

class Billing(BaseModel):
    payments: List

class TransactionResponse(BaseModel):
    object_state: str
    status: str
    object_created: str
    object_updated: str
    object_id: str
    object_owner: str
    test: bool
    rate: str
    tracking_number: str
    tracking_status: str
    eta: Optional[str]
    tracking_url_provider: str
    label_url: str
    commercial_invoice_url: Optional[str]
    messages: List[Message]
    order: Optional[str]
    metadata: str
    parcel: str
    billing: Billing
    qr_code_url: Optional[str]
    created_by: CreatedBy 