import sqlite3
import create_tables
from api_key import api_key
import api_calls
import sql_queries


if __name__ == '__main__':

    """Create/Connect to DB"""
    try:
        conn = sqlite3.connect('./timezone.db')
        c = conn.cursor()
    except Exception as e:
        print("UNABLE TO CONNECT TO DATABASE")
        print(e)

    """Create tables initially and clearing timezone table upon each time script runs. """
    try:
        create_tables.create_timezone_table(c)
        create_tables.create_details_table(c)
        create_tables.create_error_table(c)
        conn.commit()
    except Exception as e:
        sql_queries.insert_error("Error creating tables. ERROR_MSG:" + str(e), c, conn)

    """CALL GET METHOD TO GET LIST OF TIME ZONES THEN PARSE THAT LIST AND INSERT INTO DATABASE"""
    try:
        time_zone_response = api_calls.get_time_zone_list(api_key)
        sql_queries.insert_into_timezones(time_zone_response, c, conn)
    except Exception as e:
        sql_queries.insert_error("Error with GET method  or"
                                 " Inserting afterwards for TimeZone table. ERROR_MSG: " + str(e), c, conn)

    try:
        """Query Details table to get all the zonenames"""
        detail_list = c.execute(''' SELECT ZONENAME from  TZDB_ZONE_DETAILS; ''').fetchall()

        """Turning list of tuples in a list to see if the to be inserted detail is already in the table or not."""
        detail_into_list = [x[0] for x in detail_list]
    except Exception as e:
        sql_queries.insert_error("Error with querying existing timezone names and parsing into a list. "
                                 "ERROR_MSG: " + str(e), c, conn)

    try:
        """Insert function taking in the list new timezone names a connection cursor and a list of known time zone 
        names """
        sql_queries.insert_into_details(time_zone_response, c, detail_into_list, conn)
    except Exception as e:
        sql_queries.insert_error("Error GET method for GET_ZONE or inserting into Details table."
                                 "ERROR_MSG: " + str(e), c, conn)
    conn.commit()
