from .db import db

class myretail(db.Document):
    product_id=db.LongField(required=True, unique=True)
    product_price=db.DecimalField(required=True)
    product_currency_code=db.StringField(required=True)
