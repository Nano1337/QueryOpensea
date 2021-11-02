# Future developments can include getting total wallet (including tokens) or tracking multiple wallets
import requests

params = {
    'collection': 'the-wanderers',
    'limit': 1
}

r = requests.get("https://api.opensea.io/api/v1/assets", params=params)

print(r.json())
# def current_price():
#
# if __name__ == "__main__":
#     print("Hello World")
# input opensea link or api call results
# pull all NFTs from a single wallet
# create webapp to list individual prices of each NFT and total price at end
# compare last sold price and current lowest listing price and take the min of both values
# return min


