from flask import Flask, request, Response, jsonify
from database.models import myretail
from flask_restx import Namespace,Resource,reqparse,fields
from myretailapi import api
from decimal import Decimal
import logging
import requests
import pyjq
import simplejson as json

log = logging.getLogger(__name__)

pricing_details = api.model("Current Price",{
                  "value": fields.Float(required=True, description='Product Price'),
                  "currency_code": fields.String(description='Product Currency Code')
                 })

product_fields = api.model('Product Price Details',{
             "id": fields.Integer(description='Product Id'),
             "current_price": fields.Nested(pricing_details)
             })

product_output_fields = api.model('Product Price Details',{
             "id": fields.Integer(description='Product Id'),
             "name": fields.String(description='Product Description'),
             "current_price": fields.Nested(pricing_details)
             })


class Products(Resource):
    def get(self):
       ''' List all Products'''
       products=myretail.objects().to_json()
       return Response(products, mimetype="application/json", status=200)

class Product(Resource):
    INTERNAL_TARGET_URL='https://redsky-uat.perf.target.com/redsky_aggregations/v1/redsky/case_study_v1?key=3yUxt7WltYG7MFKPp7uyELi1K40ad2ys&tcin={productid}'

    def _get_reponse(self, url, params=None):
        self._session=requests.Session()
        res = self._session.get(url, params=params or {}, headers={'Accept': 'application/json'})
        if res.status_code != 200:
            raise Exception(res.reason)
        return res
 
    def get_product_details(self, id):
        url=self.INTERNAL_TARGET_URL.format(productid=id)
        response={}
        product_final_details={}
        pricing_details_dict={}
        try:
            response=self._get_reponse(url).json()
        except:
            api.abort(code=400, message="Product Id not found")
            log.exception("Product Id not found") 
        raw_dict=pyjq.first("{id: .data.product.tcin,name: .data.product.item.product_description.title}",response)
        if myretail.objects(product_id=id).count() == 1:
            log.info("Product_id exists in the database..")
            db_pricing_details=myretail.objects(product_id=id).only('product_price','product_currency_code').to_json()
            pricing_details_dict=pyjq.first(".[] | {value: .product_price, currency_code: .product_currency_code}",json.loads(db_pricing_details))
        log.debug(pricing_details_dict)
        
        product_final_details["id"]=int(raw_dict["id"])
        product_final_details["name"]=raw_dict["name"]
        product_final_details["current_price"]=pricing_details_dict
        log.debug(product_final_details)
        json_object=json.dumps(product_final_details)
        return json_object

    #@api.marshal_with(product_fields)
    def get(self, id):
        '''
        Gets Product details including current price with currency code
        '''
        return Response(self.get_product_details(id),mimetype="application/json",status=200)

    @api.expect(product_fields)
    #@api.marshal_with(product_output_fields)
    def put(self, id):
        '''
        Updates the Product price for the given Product Id.
        '''  
        body = request.get_json()
        if not body['current_price']['value']:
             api.abort(code=404, message="Product Price not found in JSON put message") 
        try:
            price_json=pyjq.first("{product_price: .current_price.value}",body)
            if price_json['product_price']:
                log.info("Ready to update") 
            else:
                api.abort(code=500, message="Product Price not found in JSON put message")
            if myretail.objects(product_id=id).count() == 1:
                myretail.objects.get(product_id=id).update(**price_json)
                json_object=self.get_product_details(id)
                return Response(self.get_product_details(id),mimetype="application/json",status=200)
            else:
                api.abort(code=404, message="Product Pricing not found in the database")
        except Exception as ex:
            log.exception(str(ex)) 
            api.abort(code=500, message="Something has gone wrong with the request")
