import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY   

ca = certifi.where() # ye certificate authority certificate ko load karta hai avoid karene ke liye timeout error when connecting mongodb

class MongoDBClient:
    client = None

    def __init__(self, database_name:str= DATABASE_NAME) -> None:

        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set")
                
                # established new connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

            # agar cilent hai tou usko use karo
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")

        except Exception as e:
            raise MyException(e, sys)




