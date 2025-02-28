MOCK_TRACKING_NUMBERS = ["SHIPPO_PRE_TRANSIT", "SHIPPO_TRANSIT", "SHIPPO_DELIVERED", "SHIPPO_RETURNED", "SHIPPO_FAILURE", "SHIPPO_UNKNOWN"]

BOOKING_PAYLOAD_TEMPLATE = {
    "parcels": [
        {
            "height": 12.5,
            "distance_unit": "in",
            "length": 12.5,
            "width": 6,
            "weight": 12,
            "mass_unit": "lb"
        }
    ],
    "address_from": {
        "name": "Mr. Hippo",
        "street1": "215 Clayton St.",
        "city": "San Francisco",
        "state": "CA",
        "zip": "94117",
        "country": "US",
        "phone": "+1 555 341 9393",
        "email": "support@shippo.com"
    },
    "address_to": {
        "name": "John K",
        "street1": "800 René-Lévesque West",
        "city": "Montreal",
        "state": "QC",
        "zip": "H3B 3B0",
        "country": "CA",
        "phone": "4215559099",
        "email": "support@shippo.com"
    },
    "object_purpose": "PURCHASE"
}