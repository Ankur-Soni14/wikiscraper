import requests
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin'
response = requests.get(bitcoin_api_url)
print(response.text)
