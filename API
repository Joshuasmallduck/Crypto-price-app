import requests
from crypto import crypto_mapping 
#above - this connects to the other file which contains every type over 400 of crypto this app can get prices for.

def get_price(symbol):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' #replace with your URL.

    parameters = {
        'symbol': symbol
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '<<enter your api key here>>' #get it from coinmarketcap and get the quote api in the latest mode.
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

price = get_price(currency_symbol)

if price is not None:
    print(f"The current price of {input_currency.capitalize()} ({currency_symbol}) is: ${price}")
else:
    print("Failed to retrieve the price.")
