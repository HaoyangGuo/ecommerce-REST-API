# Flask REST API
This is a functional REST API built with Flask and deployed on heroku. This API is designed and implemented for an imaginary online store, so it allows users to create accounts, authenticate, and interact with stores and items. 

## authentication
### register
```
curl -d 'username=YOUR_USER_NAME&password=YOUR_PASSWORD' https://test-rest-api-stores.herokuapp.com/Register
```
### authenticate
```
curl -d 'username=YOUR_USER_NAME&password=YOUR_PASSWORD' https://test-rest-api-stores.herokuapp.com/auth
```

## store(s)
### get all stores
```
curl -v https://test-rest-api-stores.herokuapp.com/stores
```
### post a store
```
curl -d 'name=YOUR_STORE_NAME' https://test-rest-api-stores.herokuapp.com/YOUR_STORE_NAME
```
### get a store
```
curl -v https://test-rest-api-stores.herokuapp.com/YOUR_STORE_NAME
```
### put a store
```
curl -X PUT 'name=YOUR_STORE_NAME' https://test-rest-api-stores.herokuapp.com/YOUR_STORE_NAME
```
### delete a store
```
curl -X DELETE https://test-rest-api-stores.herokuapp.com/YOUR_STORE_NAME
```

## item(s)
### get all items
```
curl -v https://test-rest-api-stores.herokuapp.com/items
```
### post an item
```
curl -d 'price=YOUR_PRICE&store_id=YOUR_STORE_ID' https://test-rest-api-stores.herokuapp.com/YOUR_ITEM_NAME
```
### post an item
```
curl -v https://test-rest-api-stores.herokuapp.com/YOUR_ITEM_NAME
```
### post an item
```
curl -X PUT 'price=YOUR_PRICE&store_id=YOUR_STORE_ID' https://test-rest-api-stores.herokuapp.com/YOUR_ITEM_NAME
```
### post an item
```
curl -X DELETE https://test-rest-api-stores.herokuapp.com/YOUR_ITEM_NAME
```

