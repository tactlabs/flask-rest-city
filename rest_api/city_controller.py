'''
    Notes:
    
    City code can be copied from here
        http://www.nationsonline.org/oneworld/IATA_Codes/IATA_Code_M.htm
'''

from . import api
from flask import current_app as app
from flask import request
from .response_utils import JSON_MIME_TYPE, success_, success_json

'''
    /city/test
    http://127.0.0.1:5000/city/test
'''
@api.route('/city/test')
def test1():   
    
    c = 6 + 8

    result_json = {
        'result': c,
        
        'api_error': 0
    }
    
    return success_json(result_json)


'''
    /city/get/iata/code
    http://127.0.0.1:5000/city/get/iata/code
    http://127.0.0.1:5000/city/get/iata/code?city=Chennai
    
    source: http://www.nationsonline.org/oneworld/IATA_Codes/IATA_Code_M.htm
    
    To Do:
        Read the City codes by using BeautifulSoup and then return the code
'''
@api.route('/city/get/iata/code')
def get_city_code():   
    
    city = request.args.get('city')
    
    if(city is None):
        result_json = {                
            'api_error': 102,
            'api_error_message': 'City is Empty'
        }
    
        return success_json(result_json)        
    
    city_code = '-'
    
    if(city.lower() == 'chennai'):
        city_code = 'MAA'

    result_json = {
        'city': city,
        'city_code': city_code,
        
        'api_error': 0
    }
    
    return success_json(result_json)
