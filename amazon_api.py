from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.get_items_request import GetItemsRequest
from paapi5_python_sdk.get_items_resource import GetItemsResource
from paapi5_python_sdk.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException
from constants import *
import re

class AmazonAPI:

    def __init__(self):
        self.api = DefaultApi(
        access_key=AMAZON_ACCESS_KEY, secret_key=AMAZON_SECRET_KEY, host=AMAZON_HOST, region=AMAZON_REGION
    )
    
    def get_product_from_url(self, url):
        #specify the resources you want to retrieve
        get_items_resource = [
            GetItemsResource.ITEMINFO_TITLE,
            GetItemsResource.OFFERS_LISTINGS_PRICE,
            GetItemsResource.IMAGES_VARIANTS_MEDIUM,
        ]
             
        asin = re.search(r"(?<=dp/)[A-Z0-9]{10}", url)
        if asin is None:
            asin = re.search(r"(?<=product/)[A-Z0-9]{10}", url)
        if asin is not None:
            asin = asin.group()
        else:
            print("ASIN not found in URL")
            return None
        
        #create the request
        request = GetItemsRequest(partner_tag=PARTNER_TAG, partner_type=PartnerType.ASSOCIATES, marketplace="www.amazon.it", item_ids=[asin], resources=get_items_resource)


        try:
            #get the product information
            response = self.api.get_items(request)
            product = response.items_result.items[0]
            return product
        except ApiException as e:
            print("Exception when calling DefaultApi->get_items: %s\n" % e)
            return None