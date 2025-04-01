import requests
import random
import time

# Define the endpoint
url = "http://127.0.0.1:8003/insert-mortgage-record"

# Function to generate random mortgage data
def generate_random_data():
    return {
        "credit_score": random.randint(300, 850),
        "loan_amount": random.randint(50000, 1000000),  # Loan between 50k and 1M
        "property_value": random.randint(50000, 2000000),  # Property value between 50k and 2M
        "annual_income": random.randint(20000, 500000),  # Income between 20k and 500k
        "debt_amount": random.randint(1000, 500000),  # Debt between 1k and 500k
        "loan_type": random.choice(["fixed", "adjustable"]),
        "property_type": random.choice(["condo", "single_family", "multi_family"])
    }

# Send 1000 POST requests
for i in range(1000):
    data = generate_random_data()
    response = requests.post(url, json=data)
    print(f"Request {i+1}: Status {response.status_code}, Response: {response.text}")
    time.sleep(0.1)  # Add a slight delay to avoid overloading the server
