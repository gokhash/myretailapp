import logging
from .products import Products,Product

log = logging.getLogger(__name__)

def initialize_routes(api):
    api.add_resource(Products,'/api/products')
    api.add_resource(Product,'/api/product/<id>')
