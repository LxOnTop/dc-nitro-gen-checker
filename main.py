import requests
import random
import time

# Discord Webhook URLs
valid_webhook_url = input(" Valid webhook: ")
invalid_webhook_url = input("invalid webhook: ")

# Function to check validity of a Discord Nitro code
def check_code(code):
    headers = {"Content-Type": "application/json", "Authorization": None}
    r = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}", headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

# Ask user for number of codes to generate
num_codes = int(input("How many codes would you like to generate? "))

# Generate and check codes
valid_codes = []
invalid_codes = []
for i in range(num_codes):
    # Generate a random code
    code = "discord.gift/"
    for j in range(16):
        code += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    print(f"Checking code {code}...")
    
    # Check the code's validity
    if check_code(code):
        print(f"Code {code} is valid!")
        valid_codes.append(code)
        # Send valid code to valid Webhook
        data = {"content": f"Valid code found: {code}"}
        requests.post(valid_webhook_url, json=data)
    else:
        print(f"Code {code} is invalid.")
        invalid_codes.append(code)
        # Send invalid code to invalid Webhook
        data = {"content": f"Invalid code found: {code}"}
        requests.post(invalid_webhook_url, json=data)
    
    # Wait for a short time to avoid rate limiting
    time.sleep(1)

# Print the list of valid and invalid codes
print("\nValid Codes:")
for code in valid_codes:
    print(code)

print("\nInvalid Codes:")
for code in invalid_codes:
    print(code)
