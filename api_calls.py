import requests
import time

def get_time_zone_list(key):
    parameters = {
        'key': key,
        'format': 'json'
    }
    response = requests.get('http://api.timezonedb.com/v2.1/list-time-zone', params=parameters)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("STATUS CODE NOT 200. STATUS CODE: " + str(response.status_code))


def get_details(key, zones):
    parameters = {
        'key': key,
        'format': 'json',
        'by': 'zone',
        'zone': zones
    }
    response = requests.get('http://api.timezonedb.com/v2.1/get-time-zone', params=parameters)
    time.sleep(2)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("STATUS CODE NOT 200. STATUS CODE: " + str(response.status_code))
