import requests
import time

def get_time_zone_list(key):
    parameters = {
        'key': key,
        'format': 'json'
    }
    response = requests.get('http://api.timezonedb.com/v2.1/list-time-zone', params=parameters)
    return response.json()


def get_details(key, zones):
    parameters = {
        'key': key,
        'format': 'json',
        'by': 'zone',
        'zone': zones
    }
    response = requests.get('http://api.timezonedb.com/v2.1/get-time-zone', params=parameters)
    time.sleep(2)
    return response.json()
