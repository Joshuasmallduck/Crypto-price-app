import requests
import time
from datetime import timedelta, datetime
from crypto import crypto_mapping
from my_email import email_alert  # Replace 'your_email_module' with the actual name of your module

def get_price(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol': symbol
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '7d5862d0-ae56-4616-8670-a0c5143f2cd0'
    }

    response = requests.get(url, params=parameters, headers=headers)

    if response.status_code == 200:
        data = response.json()
        quote = data.get('data', {}).get(symbol, {}).get('quote', {}).get('USD', {})
        price = quote.get('price')
        return price
    else:
        print(f"Error: {response.status_code}")
        return None

def send_email_updates(subject, body, to):
    user = 'Joshuasmallnyc@gmail.com'
    email_alert(subject, body, user)

input_currency = input("Please give me a cryptocurrency name or symbol: ")

# Assuming crypto_mapping is a dictionary defined in crypto.py
currency_symbol = crypto_mapping.get(input_currency.lower())

if currency_symbol is None:
    # Check if input is a cryptocurrency symbol
    if input_currency.upper() in crypto_mapping.values():
        currency_symbol = input_currency.upper()
    else:
        print("Unsupported cryptocurrency.")
        exit()

# Get the current price and display it
price = get_price(currency_symbol)

if price is not None:
    print(f"The current price of {input_currency.capitalize()} ({currency_symbol}) is: ${price}")
else:
    print("Failed to retrieve the price.")

# Get user input for email updates
answer_email = input("Do you want to receive email updates on this crypto? (Yes or No): ").lower()

if answer_email == "yes":
    user_email = input("What is your email? ")
    frequency_minutes = int(input("How often in minutes do you want to receive updates? "))
    duration_days = int(input("For how many days do you want to receive updates? "))

    # Main loop for sending email updates
    for _ in range(duration_days * 24 * 60 // frequency_minutes):
        price = get_price(currency_symbol)

        if price is not None:
            subject = f"The current price of {currency_symbol}"
            body = f"The current price is: ${price}"
            send_email_updates(subject, body, user_email)
        else:
            print("Failed to retrieve the price.")

        # Wait for the specified frequency
        time.sleep(frequency_minutes * 60)

    print(f"You will receive email updates every {frequency_minutes} minutes for {duration_days} days.")
else:
    print("No email updates requested.")
