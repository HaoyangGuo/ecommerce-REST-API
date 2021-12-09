# REST API
This is a functional REST API built with Flask and deployed on heroku. This API is designed and implemented for an imaginary online store, so it allows users to create accounts, authenticate, and interact with stores and items. 

## Endpoints:
https://test-rest-api-stores.herokuapp.com
### security
- /Register - POST, parameters: {"username": YOUR_USER_NAME, "password": YOUR_PASSWORD}
- /auth - POST, parameters: {"username": YOUR_USER_NAME, "password": YOUR_PASSWORD}

### store(s)
- /stores - GET 
- /store/<store_name> - GET
- /store/<store_name> - POST
- /store/<store_name> - DELETE

### item(s)
- /items - GET 
- /item/<item_name> - GET, jwt token required 
- /item/<item_name> - POST, parameters: {"price":YOUR_PRICE, "store_id":YOUR_STORE_ID}, jwt token required 
- /item/<item_name> - PUT, parameters:{"price":YOUR_PRICE, "store_id":YOUR_STORE_ID}, jwt token required 
- /item/<item_name> - DELETE, jwt token required 

