# File: /uber-motorista-fixo/uber-motorista-fixo/src/types/index.py

# Constants for pricing and client information
PRICING_PER_KM = 2.50  # Price per kilometer in currency
MINIMUM_FARE = 10.00    # Minimum fare for any ride
LOYALTY_DISCOUNT = 0.10  # 10% discount for fixed clients
PROMOTIONAL_OFFER = 0.15  # 15% discount for first ride of new clients

# Client data structure
class Client:
    def __init__(self, name, phone, is_fixed_client=False):
        self.name = name
        self.phone = phone
        self.is_fixed_client = is_fixed_client

# Function to calculate fare based on distance
def calculate_fare(distance_km, is_fixed_client):
    fare = distance_km * PRICING_PER_KM
    if fare < MINIMUM_FARE:
        return MINIMUM_FARE
    if is_fixed_client:
        fare *= (1 - LOYALTY_DISCOUNT)
    return fare

# Function to apply promotional offers
def apply_promotional_offer(is_new_client, fare):
    if is_new_client:
        fare *= (1 - PROMOTIONAL_OFFER)
    return fare