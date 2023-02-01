import sqlite3


def create_timezone_table(c):
    try:
        c.execute('''
        CREATE TABLE TZDB_TIMEZONES (
            ZONENAME  VARCHAR2(100) PRIMARY KEY,
            COUNTRYCODE VARCHAR2(2) NOT NULL,
            COUNTRYNAME VARCHAR2(100) NOT NULL,
            GMTOFFSET NUMBER,
            IMPORT_DATE  DATE
        );
                  ''')
    except sqlite3.OperationalError as e:
        c.execute('''DROP TABLE TZDB_TIMEZONES ''')

        c.execute('''
        CREATE TABLE TZDB_TIMEZONES (
            ZONENAME  VARCHAR2(100) PRIMARY KEY,
            COUNTRYCODE VARCHAR2(2) NOT NULL,
            COUNTRYNAME VARCHAR2(100) NOT NULL,
            GMTOFFSET NUMBER,
            IMPORT_DATE  DATE
        );
                  ''')

def create_details_table(c):
    try:
        c.execute('''
        CREATE TABLE TZDB_ZONE_DETAILS (
            ZONENAME varchar2(100) ,
            ZONESTART number ,
            ZONEEND number ,
            COUNTRYCODE varchar2(2) NOT NULL,
            COUNTRYNAME varchar2(100) NOT NULL,
            GMTOFFSET number,
            DST number,
            IMPORT_DATE date,
            primary key (ZONENAME, ZONESTART, ZONEEND)
        );
                  ''')
    except sqlite3.OperationalError:
        pass
    except Exception as e:
        print(e)


def create_error_table(c):
    try:
        c.execute('''
        CREATE TABLE TZDB_ERROR_LOG (
        ERROR_DATE date,
        ERROR_MESSAGE varchar2(1000)
        );
                  ''')
    except sqlite3.OperationalError:
        pass
    except Exception as e:
        print(e)