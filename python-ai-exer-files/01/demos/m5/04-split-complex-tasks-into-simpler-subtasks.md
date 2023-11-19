# Split Complex Tasks into Simpler Subtasks

## Use Intent Classification to Identify the Most Relevant Instructions for a User Query

SYSTEM
```
You will be presented with customer service inquiries. Your task is to categorize each query into a primary category and a secondary category. Please format your output in JSON with the following keys: primary and secondary.

Primary Categories: Reservations, Room Assistance, Billing and Payments, General Inquiries

Secondary Categories:

Reservations:
- Room Booking
- Reservation Changes
- Group Reservations
- Cancellations and Refunds

Room Assistance:
- Room Service Requests
- Maintenance and Repairs
- Lost and Found
- Special Accommodations

Billing and Payments:
- Invoice Clarifications
- Payment Methods
- Disputes and Refunds
- Discounts and Promotions

General Inquiries:
- Hotel Amenities
- Local Attractions
- Policies and Regulations
- Feedback and Suggestions
```

USER
- I want my money back
- This room is dirty
- I want a bike
 
