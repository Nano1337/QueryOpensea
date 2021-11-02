import streamlit as st
import requests

endpoint = st.sidebar.selectbox("Endpoints", ['Assets', 'Watchlist'])
st.header(f"OpenSea NFT API Explorer - {endpoint}")

if endpoint == 'Assets':
    collection = st.sidebar.text_input("Collection")
    owner = st.sidebar.text_input("Owner")
    params = {}

    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner

    # params = { #current_price in "sell_orders" array is in wei but convert to eth
    #     'collection': 'parallelalpha',
    #     'limit': 1
    # }

    r = requests.get("https://api.opensea.io/api/v1/assets", params=params)
    response = r.json()
    for asset in response["assets"]:
        st.image(asset['image_url'])
    st.write(r.json())

if endpoint == 'Watchlist':
    nft_ids = [10368, 10294]
    responses = []
    for nft_id in nft_ids:
        responses.append(requests.get("https://api.opensea.io/api/v1/asset/0x76be3b62873462d2142405439777e971754e8e77/" + str(nft_id)).json())
    for response in responses:
        st.image(response["image_url"])



