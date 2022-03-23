# myretailapp
## Case Study | myRetailApp RESTful service

This application is a RESTful API service that provides Retail Product information by querying internal APIs and a NO-SQL database.

#### Solution:

1.	Retrieve product and product price details by Product Id
2.	Updates the price information in the database
3.	Retrieves all product details from the database.

|Method     |Request          |Description                                            | 
|-----------|-----------------|-------------------------------------------------------|
|GET        |/api/product/{id}| Gets Production information with Price                |
|GET        |/api/products    | Gets all Product Pricing information from the database|
|PUT        |/api/product/{id}| Updates Production Price for a given Product Id       | 

#### Techology Stack

1.	Python 3.8.10 (All python modules needed are specified in requirements.txt)
    - PyJq   (Binding for jq JSON processor https://github.com/doloopwhile/pyjq)
    - FlaskRestx (https://flask-restx.readthedocs.io/en/latest/)
    - python_mongoengine (https://pypi.org/project/mongoengine/)
    - requests (https://pypi.org/project/requests/)
2.	MongoDB (https://docs.mongodb.com/)
3.	Docker

#### Setup Instructions:

###### Pre-requisites
  1. Docker
  2. GIT
  3. docker-compose
	
This is a docker application that runs on Ubuntu 20.04. 
Please download the project from the following git repository 
You can download as a ZIP file or can just clone the repository using GIT.

###### To run the application
```
myretailapp> docker-compose -up
```

###### To stop the application
```
myretailapp> docker-compose down
```

###### Examples:

1. Get Product Information from internal website and Pricing

```
curl http://localhost:5000/api/product/13264003

```
2. Update Product Price for a given Product Id and display the updated Product information
```
curl -X PUT -H "Content-Type: application/json" -d '{"id":54456119, "current_price": {"value": 5.88, "currency_code": "USD"}}' http://localhost:5000/api/product/54456119
```
###### Swagger Documentation

![Alt text](myretailapp/docs/myretail_get.gif)




