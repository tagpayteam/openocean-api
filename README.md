# openocean-api
OpenOcean Swagger API Spec

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openocean_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openocean_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openocean_api
from openocean_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openocean_api.CrossApi(openocean_api.ApiClient(configuration))
chain_id = 8.14 # float | eg:56 chainId 
hash = 'hash_example' # str | eg:0xb6a66f9676ed430407bc8b96063c8aab5ca663c45ec5d63047ade44061475e4a 

try:
    # get cross status 
    api_instance.controller_cross_get_cross_status(chain_id, hash)
except ApiException as e:
    print("Exception when calling CrossApi->controller_cross_get_cross_status: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://open-api.openocean.finance*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CrossApi* | [**controller_cross_get_cross_status**](docs/CrossApi.md#controller_cross_get_cross_status) | **GET** /cross_chain/v1/cross/getCrossStatus | get cross status 
*CrossApi* | [**controller_cross_get_cross_transaction**](docs/CrossApi.md#controller_cross_get_cross_transaction) | **GET** /cross_chain/v1/cross/getCrossTransaction | get cross transaction 
*CrossApi* | [**controller_cross_min_send**](docs/CrossApi.md#controller_cross_min_send) | **GET** /cross_chain/v1/cross/getMinSend | get min send 
*CrossApi* | [**controller_cross_quote_by_oo**](docs/CrossApi.md#controller_cross_quote_by_oo) | **GET** /cross_chain/v1/cross/quoteByOO | cross route 
*LimitOrderApi* | [**controller_limit_order_create**](docs/LimitOrderApi.md#controller_limit_order_create) | **GET** /v1/{chainId}/limit-order/address/{address} | list by address 
*LimitOrderApi* | [**controller_limit_order_update**](docs/LimitOrderApi.md#controller_limit_order_update) | **GET** /v1/{chainId}/limit-order/all | list all 
*NftApi* | [**controller_nft_assets**](docs/NftApi.md#controller_nft_assets) | **POST** /nft/v1/{chain}/sell | Create Listing 
*NftApi* | [**controller_nft_buy**](docs/NftApi.md#controller_nft_buy) | **POST** /nft/v1/{chain}/sign | Submit Order 
*NftApi* | [**controller_nft_check_order**](docs/NftApi.md#controller_nft_check_order) | **POST** /nft/v1/{chain}/offer | Create Offer 
*NftApi* | [**controller_nft_collections**](docs/NftApi.md#controller_nft_collections) | **POST** /nft/v1/{chain}/buy | Buy 
*NftApi* | [**controller_nft_detail**](docs/NftApi.md#controller_nft_detail) | **GET** /nft/v1/{chain}/detail | NFT Detail 
*NftApi* | [**controller_nft_get_delta_and_curve_type**](docs/NftApi.md#controller_nft_get_delta_and_curve_type) | **GET** /nft/v2/{chain}/collections | Collections 
*NftApi* | [**controller_nft_get_orders**](docs/NftApi.md#controller_nft_get_orders) | **GET** /nft/v1/{chain}/listings | Listings 
*NftApi* | [**controller_nft_import_asset**](docs/NftApi.md#controller_nft_import_asset) | **POST** /nft/v1/{chain}/order/state | Order Status 
*NftApi* | [**controller_nft_offer**](docs/NftApi.md#controller_nft_offer) | **POST** /nft/v1/{chain}/swap | Swap Token 
*NftApi* | [**controller_nft_orders**](docs/NftApi.md#controller_nft_orders) | **GET** /nft/v2/{chain}/orders | NFT Orders 
*NftApi* | [**controller_nft_quote**](docs/NftApi.md#controller_nft_quote) | **GET** /nft/v1/{chain}/address/activity | User Activity 
*NftApi* | [**controller_nft_rankings**](docs/NftApi.md#controller_nft_rankings) | **GET** /nft/v2/{chain}/rankings | Rankings 
*NftApi* | [**controller_nft_report**](docs/NftApi.md#controller_nft_report) | **GET** /nft/v1/{chain}/nfts | NFTs 
*NftApi* | [**controller_nft_sell**](docs/NftApi.md#controller_nft_sell) | **POST** /nft/v1/{chain}/quote | Quote Token 
*NftApi* | [**controller_nft_sign**](docs/NftApi.md#controller_nft_sign) | **POST** /nft/v1/{chain}/cancel | Cancel 
*NftApi* | [**controller_nft_swap**](docs/NftApi.md#controller_nft_swap) | **GET** /nft/v1/{chain}/collection/activity | Collection Activity 
*NftApi* | [**controller_nft_testscan**](docs/NftApi.md#controller_nft_testscan) | **GET** /nft/v1/{chain}/offers | Offers 
*SwapApi* | [**controller_swap_dex_list**](docs/SwapApi.md#controller_swap_dex_list) | **GET** /v3/{chain}/dexList | dexList 
*SwapApi* | [**controller_swap_get_transaction**](docs/SwapApi.md#controller_swap_get_transaction) | **GET** /v3/{chain}/getTransaction | getTransaction 
*SwapApi* | [**controller_swap_quote**](docs/SwapApi.md#controller_swap_quote) | **GET** /v3/{chain}/quote | quote 
*SwapApi* | [**controller_swap_swap_quote**](docs/SwapApi.md#controller_swap_swap_quote) | **GET** /v3/{chain}/swap_quote | swap_quote 
*SwapApi* | [**controller_swap_token_list**](docs/SwapApi.md#controller_swap_token_list) | **GET** /v3/{chain}/tokenList | tokenList 
*WalletApi* | [**controller_wallet_create_wallet**](docs/WalletApi.md#controller_wallet_create_wallet) | **GET** /v3/{chain}/createWallet | create wallet 
*WalletApi* | [**controller_wallet_get_balance**](docs/WalletApi.md#controller_wallet_get_balance) | **GET** /v3/{chain}/getBalance | get balance 


## Documentation For Models

 - [ActivityByAddress](docs/ActivityByAddress.md)
 - [ActivityByAddressResponse](docs/ActivityByAddressResponse.md)
 - [ActivityByCollectionResponse](docs/ActivityByCollectionResponse.md)
 - [ActivityCollection](docs/ActivityCollection.md)
 - [ActivityToken](docs/ActivityToken.md)
 - [ApproveItem](docs/ApproveItem.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeValue](docs/AttributeValue.md)
 - [BuyItem](docs/BuyItem.md)
 - [BuyRequest](docs/BuyRequest.md)
 - [BuyResponse](docs/BuyResponse.md)
 - [BuyTransactionData](docs/BuyTransactionData.md)
 - [CancelRequest](docs/CancelRequest.md)
 - [CancelResponse](docs/CancelResponse.md)
 - [CancelTransactionData](docs/CancelTransactionData.md)
 - [CheckOrder](docs/CheckOrder.md)
 - [CheckOrderRequest](docs/CheckOrderRequest.md)
 - [CheckOrderResponse](docs/CheckOrderResponse.md)
 - [Collection](docs/Collection.md)
 - [CollectionFilter](docs/CollectionFilter.md)
 - [Collections](docs/Collections.md)
 - [CollectionsResponse](docs/CollectionsResponse.md)
 - [CreateWalletRequest](docs/CreateWalletRequest.md)
 - [CrossStatusRequest](docs/CrossStatusRequest.md)
 - [CrossTransactionRequest](docs/CrossTransactionRequest.md)
 - [Detail](docs/Detail.md)
 - [DetailOrder](docs/DetailOrder.md)
 - [DetailResponse](docs/DetailResponse.md)
 - [FloorPrice](docs/FloorPrice.md)
 - [GetBalaceRequest](docs/GetBalaceRequest.md)
 - [GetTransactionRequest](docs/GetTransactionRequest.md)
 - [Listings](docs/Listings.md)
 - [ListingsResponse](docs/ListingsResponse.md)
 - [MakerOrder](docs/MakerOrder.md)
 - [MarketItem](docs/MarketItem.md)
 - [Metadata](docs/Metadata.md)
 - [MinSendRequest](docs/MinSendRequest.md)
 - [Nfts](docs/Nfts.md)
 - [NftsResponse](docs/NftsResponse.md)
 - [OfferRequest](docs/OfferRequest.md)
 - [Offers](docs/Offers.md)
 - [OffersResponse](docs/OffersResponse.md)
 - [OrderData](docs/OrderData.md)
 - [OrderFilter](docs/OrderFilter.md)
 - [OrderPaymentAsset](docs/OrderPaymentAsset.md)
 - [Orders](docs/Orders.md)
 - [OrdersResponse](docs/OrdersResponse.md)
 - [Owner](docs/Owner.md)
 - [PaymentAssetItem](docs/PaymentAssetItem.md)
 - [Quote](docs/Quote.md)
 - [QuoteByOORequest](docs/QuoteByOORequest.md)
 - [QuoteRequest](docs/QuoteRequest.md)
 - [QuoteResponse](docs/QuoteResponse.md)
 - [Rankings](docs/Rankings.md)
 - [RankingsResponse](docs/RankingsResponse.md)
 - [SellItem](docs/SellItem.md)
 - [SellOrder](docs/SellOrder.md)
 - [SellRequest](docs/SellRequest.md)
 - [SellResponse](docs/SellResponse.md)
 - [SignRequest](docs/SignRequest.md)
 - [SignResponse](docs/SignResponse.md)
 - [Swap](docs/Swap.md)
 - [SwapItem](docs/SwapItem.md)
 - [SwapQuoteRequest](docs/SwapQuoteRequest.md)
 - [SwapRequest](docs/SwapRequest.md)
 - [SwapResponse](docs/SwapResponse.md)
 - [TokenListRequest](docs/TokenListRequest.md)
 - [Traits](docs/Traits.md)
 - [Volume](docs/Volume.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



