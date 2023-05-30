# TimezoneDB

To dockerize this script. You need to have docker installed on your computer. 

Clone this repository into a folder and cd into it. Run "docker-compose up" and your container will be created and run. 

If you don't want to use docker. Just clone this repository into your local system and cd into the project folder. From there run "python main.py". 


Project Overview:
1. Create a python script to query the TimezoneDB API and populate the tables TZDB_TIMEZONES
and TZDB_ZONE_DETAILS
2. Your script should handle errors when retrieving the API and log them into the table
TZDB_ERROR_LOG.
3. TZDB_TIMEZONES is to be deleted every time you script runs and populated with data from the
API.
4. TZDB_ZONE_DETAILS is to be populated incrementally, not adding rows if the data in the table
already exists.
Hint: To achieve number 4 you can create a stage table before writing into TZDB_ZONE_DETAILS.

Notes:

• To get access to the API provided by TimezoneDB go to: https://timezonedb.com and create an
account (free), you will be provided with a Key that you can use in your scripts.

• You can use your preferred database to upload the data.
There are a few endpoints to use:

  • Get List: Use this one to populate the TZDB_TIMEZONES table.
  
  • Get Time Zone: Use this one to populate TZDB_ZONE_DETAILS

![table1](https://github.com/inolo/TimezoneDB/assets/10506956/acf08d59-2bb2-410f-bcfa-0936649100b7)
![table2](https://github.com/inolo/TimezoneDB/assets/10506956/1facf722-28c6-4a9b-8b82-ba89494e1993)
