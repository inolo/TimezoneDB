from datetime import datetime
import api_calls
from api_key import api_key




def insert_error(message,c,conn):
    time_now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    c.execute(f''' 
            INSERT INTO TZDB_ERROR_LOG 
            (ERROR_DATE, ERROR_MESSAGE)
            VALUES
            ( '{time_now}','{message}');
            ''')
    conn.commit()

def insert_into_timezones(json_response, c,conn):
    try:
        for response in json_response['zones']:
            time_now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
            c.execute(f'''
            INSERT INTO TZDB_TIMEZONES
            (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, IMPORT_DATE)
            VALUES
            ('{response['countryCode']}', '{response['countryName']}', '{response['zoneName']}', 
             {response['gmtOffset']}, '{time_now}');
            ''')
    except Exception as e:
        insert_error('ERROR INSERTING INTO TZDB_TIMEZONES TABLE, ERROR :' +str(e), c,conn)


def insert_into_details(json_response, c, known_zones,conn):
    try:
        for response in json_response['zones']:
            if response['zoneName'] in known_zones:
                continue
            try:
                time_now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
                details_response = api_calls.get_details(api_key, zones=response['zoneName'])
                c.execute(f'''
                INSERT INTO TZDB_ZONE_DETAILS 
                (ZONENAME,ZONESTART,ZONEEND,COUNTRYCODE,
                 COUNTRYNAME ,GMTOFFSET ,DST,IMPORT_DATE)
                 VALUES
                 ( '{details_response['zoneName']}', '{details_response['zoneStart']}', '{details_response['zoneEnd']}',
                 '{details_response['countryCode']}', '{details_response['countryName']}', '{details_response['gmtOffset']}',
                 '{details_response['dst']}', '{time_now}' );       ''')
                conn.commit()
            except Exception as e:
                insert_error('ERROR INSERTING INTO TZDB_ZONE_DETAILS TABLE, ERROR :' + str(e), c)
            print(details_response)
    except Exception as e:
        insert_error('ERROR PARSING TIMEZONE RESPONSE, ERROR :' + str(e), c,conn)

