db = db.getSiblingDB("MY_RETAIL");
db.MY_RETAIL.drop();

db.createCollection('myretail');

db.myretail.insertMany(
[
  {
     "product_id": 13860428,
     "product_price": 13.49,
     "product_currency_code": "USD"
  },
  {
     "product_id": 54456119,
     "product_price": 6.25,
     "product_currency_code": "USD"
  },
  {
     "product_id": 13264003,
     "product_price": 8.75,
     "product_currency_code": "USD"
  },
  {
     "product_id": 12954218,
     "product_price": 5.65,
     "product_currency_code": "USD"
  }
]
);
